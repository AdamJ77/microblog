terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.78.0"
    }
  }
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}


# MODULES
module "global_setup" {
  source = "../../../global"
}


# LOCALS
locals {
  subnet_private_ip_prefixes = "10.0.0.0/26"
  vm_size                    = "Standard_B2s"
  storage_disk_type          = "Standard_LRS"
  ubuntu_version             = "22_04-lts"
}


# Configure network
resource "azurerm_subnet" "mongodb_subnet" {
  name                 = var.subnet_name
  resource_group_name  = module.global_setup.resource_group_name
  virtual_network_name = module.global_setup.virtual_network_name
  address_prefixes     = [local.subnet_private_ip_prefixes]
}

resource "azurerm_network_interface" "nic" {
  count               = var.instances_number
  name                = "mongodb-nic-${count.index}"
  location            = module.global_setup.resource_group_location
  resource_group_name = module.global_setup.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.mongodb_subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

# Create Network Security Group
resource "azurerm_network_security_group" "mongodb_nsg" {
  name                = "mongodb-nsg"
  location            = module.global_setup.resource_group_location
  resource_group_name = module.global_setup.resource_group_name
}

resource "azurerm_network_security_rule" "ssh_inbound_rule" {
  name                        = "Test-inbound-rule"
  priority                    = 100
  direction                   = "Inbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "22"
  source_address_prefix       = var.source_address_prefix
  destination_address_prefix  = "*"
  network_security_group_name = azurerm_network_security_group.mongodb_nsg.name
  resource_group_name         = module.global_setup.resource_group_name
}

resource "azurerm_network_security_rule" "outbound_rule" {
  name                        = "example-outbound-rule"
  priority                    = 200
  direction                   = "Outbound"
  access                      = "Allow"
  protocol                    = "Tcp"
  source_port_range           = "*"
  destination_port_range      = "80"
  source_address_prefix       = "*"
  destination_address_prefix  = "*"
  network_security_group_name = azurerm_network_security_group.mongodb_nsg.name
  resource_group_name         = module.global_setup.resource_group_name
}

resource "azurerm_subnet_network_security_group_association" "nsg_association" {
  subnet_id                 = azurerm_subnet.mongodb_subnet.id
  network_security_group_id = azurerm_network_security_group.mongodb_nsg.id
}


# Create Linux Virtual Machine
resource "azurerm_linux_virtual_machine" "mongodb_vm" {
  count                 = var.instances_number
  name                  = count.index == 0 ? "mongodb-${var.db_roles[0]}" : "mongodb-${var.db_roles[1]}-${count.index}"
  resource_group_name   = module.global_setup.resource_group_name
  location              = module.global_setup.resource_group_location
  size                  = local.vm_size
  admin_username        = var.admin_username
  network_interface_ids = [
    azurerm_network_interface.nic[count.index].id
  ]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file(var.ssh_public_key_path)
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = local.storage_disk_type
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = local.ubuntu_version
    version   = "latest"
  }

  tags = {
    DBRole = count.index == 0 ? var.db_roles[0] : var.db_roles[1]
    ComponentType = module.global_setup.component_type[0]
  }
}

# Create Auto-Shutdown for VMs
resource "azurerm_dev_test_global_vm_shutdown_schedule" "shutdown_all_mongodb_instances" {
  count              = var.instances_number
  virtual_machine_id = azurerm_linux_virtual_machine.mongodb_vm[count.index].id
  location           = module.global_setup.resource_group_location
  enabled            = true

  daily_recurrence_time = "0100"  # This sets the shutdown time at 1 AM CET
  timezone              = "Central European Standard Time"

  notification_settings {
    enabled = false  # Set to true and configure additional settings if notifications are needed
  }
}
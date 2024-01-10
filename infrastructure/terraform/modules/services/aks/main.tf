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


# Create AKS
resource "azurerm_kubernetes_cluster" "microblog-aks" {
  name                = "${var.cluster_name}-${var.resource_group_name}"
  location            = var.resource_group_location
  resource_group_name = var.resource_group_name
  dns_prefix          = var.dns_prefix # used to create FQDN for cluster (<dns_prefix>.<region>.azmk8s.io)

  linux_profile {
    admin_username = var.admin_username

    ssh_key {
      key_data = file(var.ssh_public_key_path)
    }
  }

  default_node_pool {
    name       = var.default_node_pool
    node_count = var.node_count
    vm_size    = var.node_vm_size
    enable_auto_scaling = true
    min_count = var.node_min_count
    max_count = var.node_max_count
  }

  # A way for AKS to interact with Azure APIs, manage Azure resources, and authenticate
  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "test"
    ComponentType = var.component_type[1]
  }
}


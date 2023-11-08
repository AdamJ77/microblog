# Create a resource group
resource "azurerm_resource_group" "main_resource_group" {
  name     = var.resource_group_name
  location = var.location
}


# Create Networking
resource "azurerm_virtual_network" "main_vnet" {
  name                = var.virtual_network_name
  resource_group_name = azurerm_resource_group.main_resource_group.name
  location            = azurerm_resource_group.main_resource_group.location
  address_space       = ["10.0.0.0/24"]
}

output "resource_group_name" {
  value = azurerm_resource_group.main_resource_group.name
}

output "virtual_network_name" {
  value = azurerm_virtual_network.main_vnet.name
}

output "resource_group_location" {
  value = azurerm_resource_group.main_resource_group.location
}

output "component_type" {
  value = var.component
}
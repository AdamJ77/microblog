output "storage_account_name" {
    value = var.storage_account_name
}

output "storage_account_access_key" {
    value     = azurerm_storage_account.tfstate_storage_account.primary_access_key
    sensitive = true
}

output "storage_container_name" {
    value = var.storage_container_name
}

output "rb_resource_group_name" {
    value = var.resource_group_name
}

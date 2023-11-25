variable environment {
    type = string
    default = "dev"
}

variable "storage_account_name" {
    type = string
    default = "terraformstatestorage"
    description = "Name for remote backend storage account"
}

variable "storage_container_name" {
    type = string
    default = "terraform-state-storage-container"
}

variable "resource_group_location" {
    type = string
    default = "westeurope"
}

variable "resource_group_name" {
    type = string
    default = "tfstate_RG"
}

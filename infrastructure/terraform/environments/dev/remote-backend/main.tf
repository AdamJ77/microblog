terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.78.0"
    }
  }
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}


locals {
  account_replication_type = "LRS"
  access_type = "private"
}

# USE SEPARATE RG FOR DEV REMOTE BACKEND INSTEAD OF GLOBAL
resource "azurerm_resource_group" "tfstate" {
  name     = var.resource_group_name
  location = var.resource_group_location
}


resource "azurerm_storage_account" "tfstate_storage_account" {
  name                     = "${var.environment}${var.storage_account_name}"
  location                 = var.resource_group_location
  resource_group_name      = azurerm_resource_group.tfstate.name
  account_tier             = "Standard"
  account_replication_type = local.account_replication_type
  tags = {
    environment = var.environment
  }
}

resource "azurerm_storage_container" "storage_container" {
  name                  = "${var.environment}-${var.storage_container_name}"
  storage_account_name  = azurerm_storage_account.tfstate_storage_account.name
  container_access_type = local.access_type
}
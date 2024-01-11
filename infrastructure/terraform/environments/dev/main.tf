provider "azurerm" {
  features {}
}

# USE REMOTE BACKEND VARS
# module "remote_backend" {
#   source = "./remote-backend"
# }


terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.78.0"
    }
  }
  backend "azurerm" {}
}

# Import global_setup
module "global_setup" {
  source = "../../global"
}

# Define locals to simplify variable passing
locals {
  resource_group_name     = module.global_setup.resource_group_name
  virtual_network_name    = module.global_setup.virtual_network_name
  resource_group_location = module.global_setup.resource_group_location
  component_type          = module.global_setup.component_type
}


module "mongodb" {
  source = "../../modules/services/database-replica-set"
  source_address_prefix   = var.source_address_prefix
  ssh_public_key_path     = var.ssh_public_key_path
  admin_username          = var.admin_username
  resource_group_name     = local.resource_group_name
  virtual_network_name    = local.virtual_network_name
  resource_group_location = local.resource_group_location
  component_type          = local.component_type
}

module "aks" {
  source = "../../modules/services/aks"
  source_address_prefix = var.source_address_prefix
  ssh_public_key_path   = var.ssh_public_key_path
  admin_username        = var.admin_username
  resource_group_name     = local.resource_group_name
  virtual_network_name    = local.virtual_network_name
  resource_group_location = local.resource_group_location
  component_type          = local.component_type
}

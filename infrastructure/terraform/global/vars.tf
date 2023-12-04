variable resource_group_name {
    type = string
    default = "Microblog1"
}

variable location {
    type = string
    default = "eastus2"
    description = "The Azure location to deploy resources in"
}

variable "virtual_network_name" {
    type = string
    default = "Microblog-VNet"
}

variable "component" {
  type = list(string)
  default = ["mongo_database"]
  description = "Database component name"
}

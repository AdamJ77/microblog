variable resource_group_name {
    type = string
    default = "Microblog"
}

variable location {
    type = string
    default = "westeurope"
    description = "The Azure location to deploy resources in"
}

variable "virtual_network_name" {
    type = string
    default = "Microblog-VNet"
}

variable "component" {
  type = list(string)
  default = ["mongo-database"]
  description = "Database component name"
}
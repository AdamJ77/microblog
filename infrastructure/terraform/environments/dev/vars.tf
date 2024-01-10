variable resource_group {
    type = string
    default = "test-RG"
}

variable environment {
    type = string
    default = "dev"
}

variable location {
    type = string
    default = "westeurope"
    description = "The Azure location to deploy resources in"
}

variable "db_roles" {
  type        = list(string)
  default     = ["primary", "secondary"]  # Optional: provide a default value
  description = "Roles for each mongo-db instance"
}

variable "component" {
  type = string
  default = "mongo-database"
  description = "Database component name"
}

variable "admin_username" {
    type = string
    description = "The username for Azure VM admin"
    sensitive = true
}

variable "source_address_prefix" {
  type = string
  description = "Source IP address allowed to make ssh connections"
  sensitive = true
}

variable "ssh_public_key_path" {
  type        = string
  description = "Path to the SSH public key"
  sensitive = true
}

variable "admin_username" {
    type = string
    sensitive = true
    description = "The username for Azure VM admin"
}

variable "db_roles" {
  type        = list(string)
  default     = ["primary", "secondary"]  # Optional: provide a default value
  description = "Roles for each mongo-db instance"
}

variable "instances_number" {
  type = number
  default = 2
  description = "Number of MongoDB instances in Replica Set"
}

variable "subnet_name" {
  type = string
  default = "mongo-db-instances-subnet"
}

variable "http_port" {
  type        = number
  default     = 80
  description = "Port number for HTTP traffic"
}

variable "vm_size" {
  type = string
  default = "Standard_B1s"
  description = "The size that you choose then determines factors such as processing power, memory, and storage capacity."
}

variable "source_address_prefix" {
  type = string
  description = "Source IP address allowed to make ssh connections"
  sensitive = true
}

variable "ssh_public_key_path" {
  description = "Path to the SSH public key"
  type        = string
  sensitive = true
}
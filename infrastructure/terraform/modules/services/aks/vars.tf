variable "node_count" {
  default = 2
  description = "Initial number of worker nodes in cluster"
}

variable "dns_prefix" {
  default = "k8stest"
}

variable "cluster_name" {
  default = "aks"
}

variable "default_node_pool" {
  default = "agentpool"
}

variable "node_min_count" {
  default = 1
  description = "Min number of nodes defined with auto-scaling"
}

variable "node_max_count" {
  default = 3
  description = "Max number of nodes defined with auto-scaling"
}

variable "subnet_name" {
  type = string
  default = "aks-subnet"
}

variable "node_vm_size" {
  type = string
  default = "Standard_b2s"
  description = "VM size where containerized applications run"
}

variable "nsg_name" {
  type = string
  default = "aks-nsg"
  description = "Name for Network Security Group"
}

# DECLARED
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
variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "backend_instance_type" {
  description = "EC2 instance type for backend"
  type        = string
  default     = "t3.small"
}

variable "db_instance_class" {
  description = "RDS instance class"
  type        = string
  default     = "db.t3.micro"
}

variable "redis_node_type" {
  description = "ElastiCache node type"
  type        = string
  default     = "cache.t3.micro"
}

variable "db_username" {
  description = "PostgreSQL master username"
  type        = string
  default     = "farmforce_admin"
}

variable "db_password" {
  description = "PostgreSQL master password"
  type        = string
  sensitive   = true
}

variable "key_pair_name" {
  description = "EC2 SSH key pair name"
  type        = string
}


variable "MasterUserPassword" {
    default = ""
}

variable "master_username" {
    default = ""
}

variable "database_name"  {
    description = "The name of the database to create"
    default = ""
}

variable "subnet_group_name"  {
    description = "The name of the subnet group"
    default = ""
}

variable "parameter_group_name"  {
    description = "The name of the parameter group"
    default = ""
}

variable "instance_class" {
    description = "Node Type of RDS"
    default = "db.t2.micro"
}

variable "publicly_accessible" {
    description = "Is database can be publicly available"
    default     = "false"
}

variable "rds_vpc_id" {
    description = "VPC where DB will be deployed and used for a security group"
    default = "vpc-73463ds"
}



variable "app_sg" {
    default = "sg-dshjs7548"
}


variable "vpc_id" {
  description = "VPC Name"
  default     = "vpc-73463ds"
}

variable "EC2_Subnets" {
  description = "List of subnets for the EC2"
  default     = "subnet-snfdm343,subnet-fjd45633"
}

variable "ELB_Subnets_Public" {
  description = "List of subnets for the LB"
  default     = "subnet-fefhei467,subnet-dhfdj67"
}


variable "Elastic_BeanStalk_ServiceRole" {
  default = "aws-elasticbeanstalk-service-role"
}

variable "EC2_KeyName" {
  default = "demo-app"
}


variable "bastion_sg" {
  default = "sg-bscvbsx67"
}
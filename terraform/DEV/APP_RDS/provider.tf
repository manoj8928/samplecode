provider "aws" {
  region = "us-east-1"
}
terraform {
             backend "s3" {
			bucket = "demo-terraform-state"
			key    = "demo-app-rds/demo-app-rds.tfstate"
			region = "us-east-1"
		}
}

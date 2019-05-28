provider "aws" {
  region = "us-east-1"
}
terraform {
             backend "s3" {
			bucket = "demo-terraform-state"
			key    = "demo-app/demo-app.tfstate"
			region = "us-east-1"
		}
}

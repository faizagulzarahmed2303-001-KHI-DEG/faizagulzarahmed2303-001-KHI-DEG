terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  }

resource "aws_s3_bucket" "s3_data" {
    bucket = "faiza-gulzar-bucket"
    acl = "private"
}



output "faiza-gulzar-bucket" {
  value = aws_s3_bucket.s3_data.id

}
 





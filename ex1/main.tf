provider "aws" {
  region = "us-east-1"
  access_key = "AKIAVU4OHK23OWYCJR26"
  secret_key = "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"
}

resource "aws_instance" "web" {
  ami = "ami-0b898040803850657"
  instance_type = "t2.micro"
  subnet_id = "subnet-018523f5b12a8b3fb"
  tags = {
    Name = var.server_name
    Project = "seva"
  }
}

variable "server_name" {
  default = "moshe"
}

output "ip_address" {
  value = aws_instance.web.public_dns
}
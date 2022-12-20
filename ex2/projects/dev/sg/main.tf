provider "aws"{
  region = "eu-west-1"
}

modouule "sg"{
  source = "../../../modules/sg"
  sg_name = var.sg_name
  sg_name_prefix = "moshe"
}
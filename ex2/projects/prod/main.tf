provider "aws"{
  region = "eu-west-1"
}

modouule "sg"{
  source = "../../../modules/sg"
  sg_name = "prod sg"
  sg_name_prefix = "david"
}
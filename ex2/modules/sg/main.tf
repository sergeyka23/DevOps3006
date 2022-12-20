resource "aws_security_group" "sg" {
  name = "${var.sg_name_prefix} ${var.sg_name}"
}

resource "aws_eip" "eip1" {
  count = var.is_eip == true ? var.amount_of_eips : 3
  tags = {
    Name = "eip number ${count.index}"
  }
}

resource "aws_security_group" "demo-app-sg" {
  name = "demo-app-sg"
  description = "Security Group for EBs INSTANCES "
  vpc_id = "${var.vpc_id}"


  ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      security_groups = ["${var.bastion_sg}"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

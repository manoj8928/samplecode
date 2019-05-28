resource "aws_db_instance" "demo" { 
    identifier              =  "demo"
    name                    = "${var.database_name}"
    username                = "${var.master_username}"
    password                = "${var.MasterUserPassword}"
    engine                  = "postgres"
    engine_version          = "9.6.6"
    license_model           = "postgresql-license"
    instance_class          = "${var.instance_class}"
    allocated_storage       = 100
    multi_az                = "false"
    port                    = 5432
    publicly_accessible     = "${var.publicly_accessible}"
    storage_type            = "gp2"
    storage_encrypted       = "true"
    db_subnet_group_name    = "${var.subnet_group_name}"
    parameter_group_name    = "${var.parameter_group_name}"
    vpc_security_group_ids  = ["${aws_security_group.demo.id}"]
    maintenance_window      = "sat:10:00-sat:11:00"
    allow_major_version_upgrade   = "false"
    auto_minor_version_upgrade    = "true"
    backup_retention_period       = 14  
    skip_final_snapshot   = "true"
}

resource "aws_security_group" "demo" {
    name    = "SG-DEMO-DB"
    description = "Security group for  database"
    vpc_id = "${var.rds_vpc_id}"

egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

ingress {
    from_port = 5432
    to_port = 5432
    protocol = "tcp"
    security_groups = [
		"${var.app_sg}"
		]
		}

 
}
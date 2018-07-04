/* Setup our aws provider */
provider "aws" {
  access_key  = "${var.access_key}"
  secret_key  = "${var.secret_key}"
  region      = "${var.region}"
}
resource "aws_instance" "jenk" {
  ami           = "${var.ami}"
  instance_type = "t2.micro"
  subnet_id = "${var.subn}"
  key_name = "${var.key}"
  associate_public_ip_address = true
  private_ip = "10.244.0.20"

  # This is where we configure the instance with ansible-playbook
  provisioner "local-exec" {
    command = "sleep 120; ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu --private-key '${var.pk}' -i '${aws_instance.jenk.private_ip},' jenk.yaml"
    }

  tags = {
    Name = "olrudenk_jenk"
  }
}



provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "vpc" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"
  tags = {
    Name = "vpc"
  }
}

resource "aws_subnet" "subnet" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = "10.0.1.0/24"
  tags = {
    Name = "subnet"
  }
}

resource "aws_security_group" "security_group" {
  vpc_id   = aws_vpc.vpc.id
  for_each = var.security_group
  name     = each.value.name
  ingress  = [for rule in each.value.ingress : rule.rules]
  egress   = [for rule in each.value.egress : rule.rules]
}

resource "aws_instance" "instances" {
  for_each               = var.instances
  ami                    = each.value.instance_ami
  instance_type          = each.value.instance_type
  subnet_id              = aws_subnet.subnet.id
  vpc_security_group_ids = [aws_security_group.security_group[each.value.security_name].id]
  tags = {
    Name = "${each.value.instance_name}"
  }
}

resource "aws_iam_user" "users" {
  for_each = { for user in var.users : user.username => user }
  name     = each.value.username
}

resource "aws_iam_access_key" "users" {
  for_each = { for user in var.users : user.username => user }
  user     = aws_iam_user.users[each.value.username].name
}

data "aws_iam_policy_document" "users" {
  for_each  = { for user in var.users : user.username => user }
  policy_id = each.value.username
  statement {
    effect    = "Allow"
    sid       = "VisualEditor0"
    actions   = each.value.restrictions.actions
    resources = each.value.restrictions.resources
  }
}

resource "aws_iam_user_policy" "users" {
  for_each = { for user in var.users : user.username => user }
  user     = aws_iam_user.users[each.value.username].name
  name     = each.value.restrictions.restriction_name
  policy   = data.aws_iam_policy_document.users[each.value.username].json
}
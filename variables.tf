variable "environment" {
  type = string
}

variable "aws_region" {
  type = string
}

variable "security_group" {
  type = map(object({

    name = string

    ingress = list(map(object({
      description      = string
      from_port        = number
      to_port          = number
      protocol         = string
      cidr_blocks      = list(string)
      ipv6_cidr_blocks = list(string)
      prefix_list_ids  = list(string)
      self             = bool
      security_groups  = list(string)
    })))

    egress = list(map(object({
      description      = string
      from_port        = number
      to_port          = number
      protocol         = string
      cidr_blocks      = list(string)
      ipv6_cidr_blocks = list(string)
      prefix_list_ids  = list(string)
      self             = bool
      security_groups  = list(string)
    })))

  }))

}

variable "instances" {
  type = map(object({
    instance_name = string
    instance_ami  = string
    instance_type = string
    security_name = string
  }))
}

variable "users" {
  type = map(object({
    username = string
    restrictions = object({
      restriction_name = string
      actions          = list(string)
      resources        = list(string)
    })
  }))
}



# Projeto Computação em Nuvem

### Feito por Carolina Hirschheimer

Este projeto foi realizado para a Disciplina de Computação em Nuvem, com objetivo de desenvolver uma aplicação capaz de provisionar uma infraestrutura por meio de uma interface amigável (livre escolha) para gerenciar e administrá-la (construir, alterar e deletar recursos).

## Preparando o ambiente de trabalho

1. Instalando Terraform

Primeiramente, deve-se instalar o Terraform, através do seguinte link: [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)

2. Acessando Dashboard AWS

Em seguida, deve-se acessar o [Dashboard AWS](https://us-east-1.signin.aws.amazon.com/oauth?response_type=code&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fec2&redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fec2%2Fhome%3Fregion%3Dus-east-1%26state%3DhashArgs%2523Instances%253A%26isauthcode%3Dtrue&forceMobileLayout=0&forceMobileApp=0&code_challenge=rfmeiMerhJv6rAAbCx-bA3qnGEMxBVpP-wFpoDcgM_M&code_challenge_method=SHA-256) e, para este projeto, foram criados usuários novos cujas credenciais foram utilizadas como ACCESS_KEY e SECRET_KEY. Ao longo do projeto, o Dashoboard foi crucial para verificação da criação de instâncias, grupos de segurança, usuários e outras features. 

3. Instalando AWS CLI

Deve-se também instalar o [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), para ter acesso às linhas de comando da AWS. 

## Configurando Credenciais 

É extremamente importante que as **credenciais AWS não sejam publicadas em um ambiente público** como o Github. Para tanto, a primeira etapa do projeto deve ser fazer o setup das credenciais AWS como variáveis locais do environment em que estamos trabalhando. Essa configuração das chaves pode ser feita pela seguinte linha de código:

```
$ aws configure --profile "choose_profile_name"
```

Após rodar a linha acima, o AWS deve solicitar as chaves de Access ID e Secret Access, conforme o exemplo a seguir:

```
AWS Acess Key ID [None]: EXAMPLEACCESSKEY
AWS Secret Acess Key [None]: ExampleSecretKey123
```

Configuradas as credenciais, é possível iniciar o projeto. 

## Como funciona o Programa 

Terraform é uma infraestrutura como código (IaaS) que permite que desenvolvedores usem uma linguagens de alto nível para criar uma infraestrutura em rede. No caso deste projeto, estamos fazendo o gerenciamento da infraestrutura através do código em Python implementado no arquivo ```main.py```.

Neste projeto, a interface em Terraform está, sobretudo, dividida em três arquivos: ```main.tf```, ```variables.tf``` e ```.auto.tfvars.json```. 

O arquivo ```main.tf``` apresenta a estrutura geral da nossa infraestrutura. Nele, é implementada a estrutura de todos os recursos configurados no nosso AWS Provider. Os recursos AWS podem ser obtidos na documentação do Terraform para AWS Providers disponível [aqui](https://registry.terraform.io/providers/hashicorp/aws/latest/docs).

O arquivo ```variables.tf```, enquanto isso, é crucial para podermos configurar o tipo de cada variável que define os recursos AWS do arquivo ```main.tf```. Veja a seguir, por exemplo, como os tipos dos recursos da variável *instances* são definidas em ```variables.tf```:

```
variable "instances" {
  type = map(object({
    instance_name = string
    instance_ami  = string
    instance_type = string
    security_name = string
  }))
}
```
Finalmente, o arquivo ```.auto.tfvars.json``` é um arquivo json que contém, de fato, os valores das variáveis cujos tipos são definidos em ```variables.tf``` e configurados na ```main.tf```. No nosso programa, esse arquivo é um dicionário definido e alterado pelo código Python da ```main.py```, que estabelece a interface com o usuário e aplica as mudanças via terraform no AWS. Veja um exemplo de como a variável *instances* apresentada acima é implementada em ```.auto.tfvars.json```:

```
"instances" : {
    "instance_1" : {
        "instance_name" : "instancia default",
        "instance_ami" : "ami-0ee23bfc74a881de5",
        "instance_type" : "t2.micro", 
        "security_name" : "standard"
    }
},
```

## Funcionalidades

Com base nessa lógica de programação, o programa em questão é capaz de realizar através da interface Python as seguintes funcionalidades, apresentadas ao rodarmos o código base:
1. Mostrar visão geral
2. Criar Instância
3. Deletar Instância
4. Listar Instâncias
5. Criar Grupo de Segurança
6. Deletar Grupo de Segurança
7. Deletar Regras de Grupo de Segurança
8. Listar Grupos de Segurança
9. Criar Usuário
10. Deletar Usuário
11. Listar Usuários
12. Sair

## Executando o Programa

Para executar um arquivo genérico terraform, deve-se executar no terminal, sequencialmente os seguintes commandos:

```
$ terraform init
$ terraform plan
$ terraform apply
```

No caso deste programa, esses arquivos são executados automaticamente pelo código python da ```main.py```. O comando ```init``` só inicializa o backend do Terraform, de modo que só precisa ser executado uma vez no início do código. Enquanto isso, o comando ```plan``` verifica todas as variáveis e recursos da infraestrutura, de modo que é executado toda vez que é realizada uma alteração. Por fim, o comando ```apply``` implementa as mudanças na rede, de modo que ele também é executado no código toda vez que é feita uma alteração de infraestrutura.

Considerando que todos esses comandos fazem parte do programa em Pyhton, o único comando que, de fato, necessitamos executar nesse projeto é:

```
$ python main.py
```



import subprocess
import shlex
import json
import time
from subprocess import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    
time.sleep(1)
auto_vars_json = open('.auto.tfvars.json')
json_dict = json.load(auto_vars_json)
auto_vars_json.close()

print(f"\n{bcolors.BOLD}{bcolors.OKBLUE}-----------------------------------------------------------------------------------{bcolors.ENDC}")
print(f"                    {bcolors.BOLD}{bcolors.OKBLUE}BEM VINDO AO PROGRAMA DE GERENCIAMENTO AWS!{bcolors.ENDC}")
print(f"{bcolors.BOLD}{bcolors.OKBLUE}-----------------------------------------------------------------------------------{bcolors.ENDC}")
print("\n")

# -------------------------------------------------------------------
# ESCOLHENDO A REGIÃO
# -------------------------------------------------------------------

print("Escolha a região em que deseja trabalhar:")
print("1. us-east-1")
print("2. us-east-2")

n_region = int(input("\nDigite aqui: "))
print("\n")

if n_region == 1:
    region = "us-east-1"

if n_region == 2:
    region = "us-east-2"

auto_vars_json = open('.auto.tfvars.json')
json_dict = json.load(auto_vars_json)
auto_vars_json.close()

json_dict["aws_region"] = region


print("---------------------Initiating in region {}----------------------".format(region))

time.sleep(0.5)

subprocess.run(shlex.split("terraform init"))

time.sleep(0.5)

n_servico = 0

# -------------------------------------------------------------------
# LOOP DE SERVIÇOS
# -------------------------------------------------------------------

while n_servico != 12:

    print(f"{bcolors.BOLD}{bcolors.OKBLUE}\nDigite o número do serviço que deseja realizar:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}{bcolors.OKBLUE}--------------------------------------------------------------{bcolors.ENDC}")
    print("1. Mostrar visão geral")
    print("2. Criar Instância")
    print("3. Deletar Instância")
    print("4. Listar Instâncias")
    print("5. Criar Grupo de Segurança")
    print("6. Deletar Grupo de Segurança")
    print("7. Deletar Regras de Grupo de Segurança")
    print("8. Listar Grupos de Segurança")
    print("9. Criar Usuário")
    print("10. Deletar Usuário")
    print("11. Listar Usuários")
    print("12. Sair")

    n_servico = int(input("\nDigite aqui: "))
    print("\n")

    # -------------------------------------------------------------------
    # 1) VISÃO GERAL
    # -------------------------------------------------------------------
    if n_servico == 1: 
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}-----------------------VISÃO GERAL-----------------------{bcolors.ENDC}")

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        # Printa região
        print(f"{bcolors.OKBLUE}\nRegião operando: {bcolors.ENDC}", json_dict["aws_region"])

        # Lista instâncias
        list_instances = list(json_dict["instances"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nAs instâncias disponíveis são:{bcolors.ENDC}")
        i=1
        for instance in list_instances:
            print("\n{}. {}".format(i, instance))

            dict_images = dict()
            dict_images["ami-0ee23bfc74a881de5"] = "Ubuntu Server 18.04 LTS, SSD Volume Type (64 bits (x86))"
            dict_images["ami-0149b2da6ceec4bb0"] = "Ubuntu Server 20.04 LTS, SSD Volume Type (64 bits (x86))"
            dict_images["ami-08c40ec9ead489470"] = "Ubuntu Server 22.04 LTS, SSD Volume Type (64 bits (x86))"
            inst_ami = json_dict["instances"][instance]["instance_ami"]
            print("   Imagem: ", dict_images[inst_ami])

            print("   Tipo: ", json_dict["instances"][instance]["instance_type"])

            print("   Grupo de Segurança: ", json_dict["instances"][instance]["security_name"])

            i+=1

        # Lista grupos de segurança
        list_grupo_seguranca = list(json_dict["security_group"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nOs grupos de segurança disponíveis são:{bcolors.ENDC}")
        i=1
        for sec_group in list_grupo_seguranca:
            print("\n{}. {}".format(i, sec_group))
            print("   Ingress Rules: ")
            print("   - Description: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["description"])
            print("   - From port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["from_port"])
            print("   - To port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["to_port"])
            print("   - Protocol: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["protocol"])
            print("   - Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["cidr_blocks"])
            print("   - IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   - Prefix List IDs: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["prefix_list_ids"])
            print("   - Self: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["self"])
            print("   - Security Groups: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["security_groups"])
            print("   Egress Rules: ")
            print("   - Description: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["description"])
            print("   - From port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["from_port"])
            print("   - To port: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["to_port"])
            print("   - Protocol: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["protocol"])
            print("   - Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["cidr_blocks"])
            print("   - IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   - Prefix List IDs: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["prefix_list_ids"])
            print("   - Self: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["self"])
            print("   - Security Groups: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["security_groups"])

            i+=1

        # Lista usuários
        list_users = list(json_dict["users"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nOs usuários disponíveis são:{bcolors.ENDC}")
        i=1
        for user in list_users:
            print("\n{}. {}".format(i, user))
            print("   Restriction Name: ", json_dict["users"][user]["restrictions"]["restriction_name"])
            print("   Action Restrictions: ", json_dict["users"][user]["restrictions"]["actions"])
            print("   Resources Restrictions: ", json_dict["users"][user]["restrictions"]["resources"])
            i+=1
        
        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 2) CRIRAR INSTÂNCIA
    # -------------------------------------------------------------------
    if n_servico == 2: 

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        print(f"{bcolors.OKBLUE}Iniciando criação de instância...{bcolors.ENDC}")

        # 1) Escolhe nome da instancia

        nome_instancia = input("\nDigite o nome da instância: ")

        # 2) Escolhe imagem da instancia

        print("\nEscolha o tipo de imagem e sistema operacional:")
        print("1. Ubuntu Server 18.04 LTS, SSD Volume Type (64 bits (x86))")
        print("2. Ubuntu Server 20.04 LTS, SSD Volume Type (64 bits (x86))")
        print("3. Ubuntu Server 22.04 LTS, SSD Volume Type (64 bits (x86))")

        imagem_instancia = int(input("\nDigite o número correspondente: "))

        if imagem_instancia == 1:
            imagem_instancia = "ami-0ee23bfc74a881de5"

        if imagem_instancia == 2:
            imagem_instancia = "ami-0149b2da6ceec4bb0"

        if imagem_instancia == 3:
            imagem_instancia = "ami-08c40ec9ead489470"
        
        # 3) Escolhe tipo de instância    
            
        print("\nEscolha o tipo instância:")
        print("1. t1.micro")
        print("2. t2.nano")

        tipo_instancia = int(input("\nDigite o número correspondente: "))

        if tipo_instancia == 1:
            tipo_instancia = "t1.micro"

        if tipo_instancia == 2:
            tipo_instancia = "t2.nano"
        
        # 4) Escolhe grupo de segurança  

        list_security_groups = list(json_dict["security_group"])

        print("\nEscolha o grupo de segurança:")

        i=1
        for security_group in list_security_groups:
            print("{}. {}".format(i, security_group))
            i+=1

        grupo_de_seguranca = int(input("\nDigite o número correspondente: "))
        grupo_de_seguranca = list_security_groups[grupo_de_seguranca-1]

        json_dict["instances"][nome_instancia] = {
                "instance_name" : nome_instancia,
                "instance_ami" : imagem_instancia,
                "instance_type" : tipo_instancia, 
                "security_name" : grupo_de_seguranca
            }
        
        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nInstância {} criada com sucesso!\n".format(nome_instancia))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 10

    # -------------------------------------------------------------------
    # 3) DELETAR INSTÂNCIA
    # -------------------------------------------------------------------
    if n_servico == 3:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_instances = list(json_dict["instances"])
        time.sleep(1)

        print("\nEscolha a instância que deseja deletar:")

        i=1
        for instance in list_instances:
            print("{}. {}".format(i, instance))
            i+=1

        instancia_a_deletar = int(input("\nDigite o número correspondente: "))
        instancia_a_deletar = list_instances[instancia_a_deletar-1]

        json_dict["instances"].pop(instancia_a_deletar)
        
        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nInstância {} deletada com sucesso!\n".format(instancia_a_deletar))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 4) LISTAR INSTÂNCIAS
    # -------------------------------------------------------------------
    if n_servico == 4:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_instances = list(json_dict["instances"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nAs instâncias disponíveis são:{bcolors.ENDC}")
        i=1
        for instance in list_instances:
            print("\n{}. {}".format(i, instance))

            dict_images = dict()
            dict_images["ami-0ee23bfc74a881de5"] = "Ubuntu Server 18.04 LTS, SSD Volume Type (64 bits (x86))"
            dict_images["ami-0149b2da6ceec4bb0"] = "Ubuntu Server 20.04 LTS, SSD Volume Type (64 bits (x86))"
            dict_images["ami-08c40ec9ead489470"] = "Ubuntu Server 22.04 LTS, SSD Volume Type (64 bits (x86))"
            inst_ami = json_dict["instances"][instance]["instance_ami"]
            print("   Imagem: ", dict_images[inst_ami])

            print("   Tipo: ", json_dict["instances"][instance]["instance_type"])

            print("   Grupo de Segurança: ", json_dict["instances"][instance]["security_name"])

            i+=1

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 5) CRIAR GRUPO DE SEGURANÇA
    # -------------------------------------------------------------------
    if n_servico == 5:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        print("Iniciando criação de grupo de segurança...")
        print("-------------------------------------------------------")

        # 1) Escolhe nome do grupo de seguranca
        nome_grupo_seguranca = input("\nDigite o nome do grupo de segurança: ")

        # 2) Define ingress variables
        print("Definição das regras de ingress")
        print("-------------------------------------------------------\n")
        ingress_description = input("Digite a description das regras ingress: ")
        ingress_from_port = input("Digite o port de saída (standard ex.: 22): ")
        ingress_to_port = input("Digite o port de destino (standard ex.: 22): ")
        ingress_protocol = input("Digite o nome do protocolo (standard ex.: tcp): ")
        ingress_cidr_blocks = json.loads(input("Digite a lista de cidr blocks (standard ex.: ['0.0.0.0/16']): "))
        ingress_ipv6_cidr_blocks = json.loads(input("Digite a configuração de ipv6 cidr blocks (standard ex.: null): "))
        ingress_prefix_list_ids = json.loads(input("Digite a lista de prefix ids (standard ex.: null): "))
        ingress_self = json.loads(input("Digite a configuração para self (standard ex.: null): "))
        ingress_security_groups = json.loads(input("Digite a configuração de security groups (standard ex.: null): "))

        # 3) Define egress variables
        print("\nDefinição das regras de egress")
        print("-------------------------------------------------------")
        egress_description = input("Digite a description das regras egress: ")
        egress_from_port = input("Digite o port de saída (ex.: 0): ")
        egress_to_port = input("Digite o port de destino (ex.: 0): ")
        egress_protocol = input("Digite o nome do protocolo (standard ex.: -1): ")
        egress_cidr_blocks = json.loads(input("Digite a lista de cidr blocks (standard ex.: ['0.0.0.0/0']): "))
        egress_ipv6_cidr_blocks = json.loads(input("Digite a configuração de ipv6 cidr blocks (standard ex.: ['::/0']): "))
        egress_prefix_list_ids = json.loads(input("Digite a lista de prefix ids (standard ex.: null): "))
        egress_self = json.loads(input("Digite a configuração para self (standard ex.: null): "))
        egress_security_groups = json.loads(input("Digite a configuração de security groups (standard ex.: null): "))

        # Preencher json_dict

        json_dict["security_group"][nome_grupo_seguranca] = {
            "name": nome_grupo_seguranca, 
            "ingress": [{
                "rules": {
                    "description": ingress_description, 
                    "from_port": ingress_from_port, 
                    "to_port": ingress_to_port, 
                    "protocol": ingress_protocol, 
                    "cidr_blocks": ingress_cidr_blocks, 
                    "ipv6_cidr_blocks": ingress_ipv6_cidr_blocks, 
                    "prefix_list_ids": ingress_prefix_list_ids, 
                    "self": ingress_self, 
                    "security_groups": ingress_security_groups
                }
            }],
            "egress" : [{
                "rules": {
                    "description"    : egress_description,
                    "from_port"      : egress_from_port,
                    "to_port"        : egress_to_port,
                    "protocol"       : egress_protocol,
                    "cidr_blocks"    : egress_cidr_blocks,
                    "ipv6_cidr_blocks" : egress_ipv6_cidr_blocks,
                    "prefix_list_ids" : egress_prefix_list_ids,
                    "self" : egress_self,
                    "security_groups" : egress_security_groups
                }
            }]
        }

        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nGrupo de segurança {} criada com sucesso!\n".format(nome_grupo_seguranca))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 6) DELETAR GRUPO DE SEGURANÇA
    # -------------------------------------------------------------------
    if n_servico == 6:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_security_groups = list(json_dict["security_group"])
        time.sleep(1)

        print("\nEscolha o grupo de segurança que deseja deletar:")

        i=1
        for security_group in list_security_groups:
            print("{}. {}".format(i, security_group))
            i+=1

        grupo_seguranca_a_deletar = int(input("\nDigite o número correspondente: "))
        grupo_seguranca_a_deletar = list_security_groups[grupo_seguranca_a_deletar-1]

        json_dict["security_group"].pop(grupo_seguranca_a_deletar)
        
        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nGrupo de segurança {} deletada com sucesso!\n".format(grupo_seguranca_a_deletar))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 7) DELETAR REGRAS DE GRUPOS DE SEGURANÇA
    # -------------------------------------------------------------------
    if n_servico == 7:
        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_grupo_seguranca = list(json_dict["security_group"])
        time.sleep(1)
        print("De qual grupo de segurança deseja deletar regras?")
        i=1
        for sec_group in list_grupo_seguranca:
            print("\n{}. {}".format(i, sec_group))

        n_sec_group = int(input("\nDigite aqui: "))

        ingress_or_egress = input("Deseja mudar deletar uma regra de ingress ou egress? (i/e)")

        if ingress_or_egress == "i":
            print("   Ingress Rules do Grupo de Segurança {}: ".format(list_grupo_seguranca[n_sec_group-1]))
            print("   a) Description: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["description"])
            print("   b) From port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["from_port"])
            print("   c) To port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["to_port"])
            print("   d) Protocol: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["protocol"])
            print("   e) Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["cidr_blocks"])
            print("   f) IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   g) Prefix List IDs: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["prefix_list_ids"])
            print("   h) Self: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["self"])
            print("   i) Security Groups: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["security_groups"])

            letra_a_deletar = input("Digita a letra (minúscula) correspondente à regra que deseja deletar: ")

            if letra_a_deletar == "a":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["description"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["description"]
            elif letra_a_deletar == "b":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["from_port"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["from_port"]
            elif letra_a_deletar == "c":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["to_port"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["to_port"]
            elif letra_a_deletar == "d":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["protocol"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["protocol"]
            elif letra_a_deletar == "e":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["cidr_blocks"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["cidr_blocks"]
            elif letra_a_deletar == "f":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["ipv6_cidr_blocks"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["ipv6_cidr_blocks"]
            elif letra_a_deletar == "g":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["prefix_list_ids"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["prefix_list_ids"]
            elif letra_a_deletar == "h":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["self"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["self"]
            elif letra_a_deletar == "i":
                json_dict["security_group"][sec_group]["ingress"][0]["rules"]["security_groups"] = json_dict["security_group"]["standard"]["ingress"][0]["rules"]["security_groups"]

        elif ingress_or_egress == "e":
            print("   egress Rules do Grupo de Segurança {}: ".format(list_grupo_seguranca[n_sec_group-1]))
            print("   a) Description: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["description"])
            print("   b) From port: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["from_port"])
            print("   c) To port: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["to_port"])
            print("   d) Protocol: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["protocol"])
            print("   e) Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["cidr_blocks"])
            print("   f) IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   g) Prefix List IDs: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["prefix_list_ids"])
            print("   h) Self: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["self"])
            print("   i) Security Groups: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["security_groups"])

            letra_a_deletar = input("Digita a letra (minúscula) correspondente à regra que deseja deletar: ")

            if letra_a_deletar == "a":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["description"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["description"]
            elif letra_a_deletar == "b":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["from_port"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["from_port"]
            elif letra_a_deletar == "c":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["to_port"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["to_port"]
            elif letra_a_deletar == "d":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["protocol"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["protocol"]
            elif letra_a_deletar == "e":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["cidr_blocks"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["cidr_blocks"]
            elif letra_a_deletar == "f":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["ipv6_cidr_blocks"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["ipv6_cidr_blocks"]
            elif letra_a_deletar == "g":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["prefix_list_ids"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["prefix_list_ids"]
            elif letra_a_deletar == "h":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["self"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["self"]
            elif letra_a_deletar == "i":
                json_dict["security_group"][sec_group]["egress"][0]["rules"]["security_groups"] = json_dict["security_group"]["standard"]["egress"][0]["rules"]["security_groups"]

        else:
            print("Input inválido")
            ingress_or_egress = input("Deseja mudar deletar uma regra de ingress ou egress? (i/e)")

        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 8) LISTAR GRUPOS DE SEGURANÇA
    # -------------------------------------------------------------------
    if n_servico == 8:
        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_grupo_seguranca = list(json_dict["security_group"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nOs grupos de segurança disponíveis são:{bcolors.ENDC}")
        i=1
        for sec_group in list_grupo_seguranca:
            print("\n{}. {}".format(i, sec_group))
            print("   Ingress Rules: ")
            print("   - Description: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["description"])
            print("   - To port: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["to_port"])
            print("   - Protocol: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["protocol"])
            print("   - Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["cidr_blocks"])
            print("   - IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   - Prefix List IDs: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["prefix_list_ids"])
            print("   - Self: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["self"])
            print("   - Security Groups: ", json_dict["security_group"][sec_group]["ingress"][0]["rules"]["security_groups"])
            print("   Egress Rules: ")
            print("   - Description: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["description"])
            print("   - To port: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["to_port"])
            print("   - Protocol: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["protocol"])
            print("   - Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["cidr_blocks"])
            print("   - IPv6 Cidr Blocks: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["ipv6_cidr_blocks"])
            print("   - Prefix List IDs: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["prefix_list_ids"])
            print("   - Self: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["self"])
            print("   - Security Groups: ", json_dict["security_group"][sec_group]["egress"][0]["rules"]["security_groups"])
            i+=1

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12


    # -------------------------------------------------------------------
    # 9) CRIAR USUÁRIO
    # -------------------------------------------------------------------
    if n_servico == 9:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        nome_usuario = input("\nDigite o nome do usuário: ")

        restricoes_sn = input("\nVocê deseja configurar restrições para o usuário (sim/nao)? ")

        if restricoes_sn == "sim":
            nome_restricao = input("\nDigite o nome da restrição: ")
            print("----- Configurando restrições de actions ------")
            new_action = "sim"
            actions = []
            while new_action == "sim":
                action = input("\nDigite a action restriction que deseja configurar (ex.: ec2:RunInstances, s3:*) ")
                actions.append(action)
                new_action = input("Deseja configurar uma nova action restriction? (sim/nao) ")
            print("----- Configurando restrições de resources ------")
            new_resource = "sim"
            resources = []
            while new_resource == "sim":
                resource = input("\nDigite o resource restriction que deseja configurar (ex.: ec2:RunInstances, s3:*) ")
                resources.append(resource)
                new_resource = input("Deseja configurar um novo resource restriction? (sim/nao) ")

        else:
            nome_restricao = "default_restrictions"
            actions = ["*"]
            resources = ["*"]

        json_dict["users"][nome_usuario] = {
                "username" : nome_usuario,
                "restrictions" : {
                    "restriction_name" : nome_restricao,
                    "actions": actions,
                    "resources": resources
                }
            }
        
        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nUsuário {} criado com sucesso!\n".format(nome_usuario))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12
    
    # -------------------------------------------------------------------
    # 10) DELETAR USUÁRIO
    # -------------------------------------------------------------------
    if n_servico == 10:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_users = list(json_dict["users"])
        time.sleep(1)

        print("\nEscolha o usuário que deseja deletar:")

        i=1
        for user in list_users:
            print("{}. {}".format(i, user))
            i+=1

        usuario_a_deletar = int(input("\nDigite o número correspondente: "))
        usuario_a_deletar = list_users[usuario_a_deletar-1]

        json_dict["users"].pop(usuario_a_deletar)
        
        with open('.auto.tfvars.json', 'w') as f:
            json.dump(json_dict, f)
        
        subprocess.run(shlex.split("terraform fmt"))
        subprocess.run(shlex.split("terraform plan"))
        subprocess.run(shlex.split("terraform apply -auto-approve"))

        print("\nUsuário {} deletada com sucesso!\n".format(usuario_a_deletar))

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

    # -------------------------------------------------------------------
    # 11) LISTAR USUÁRIOS
    # -------------------------------------------------------------------
    if n_servico == 11:

        # Carrega json atual
        auto_vars_json = open('.auto.tfvars.json')
        json_dict = json.load(auto_vars_json)
        auto_vars_json.close()

        list_users = list(json_dict["users"])
        time.sleep(1)
        print(f"{bcolors.OKBLUE}\nOs usuários disponíveis são:{bcolors.ENDC}")
        i=1
        for user in list_users:
            print("\n{}. {}".format(i, user))
            print("   Restriction Name: ", json_dict["users"][user]["restrictions"]["restriction_name"])
            print("   Action Restrictions: ", json_dict["users"][user]["restrictions"]["actions"])
            print("   Resources Restrictions: ", json_dict["users"][user]["restrictions"]["resources"])
            i+=1
        
        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

        next = int(input("\nDigite 1 para voltar ao MENU INICIAL e 2 para SAIR: "))
        if next == 2:
            n_servico = 12

print(f"\n{bcolors.BOLD}{bcolors.OKBLUE}-----------------------------------------------------------------------------------{bcolors.ENDC}")
print(f"                       {bcolors.BOLD}{bcolors.OKBLUE}PROGRAMA ENCERRADO{bcolors.ENDC}")
print(f"{bcolors.BOLD}{bcolors.OKBLUE}-----------------------------------------------------------------------------------{bcolors.ENDC}")
print("\n")
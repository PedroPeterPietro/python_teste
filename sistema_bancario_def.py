import textwrap 
import re
banco_de_dados = {}
def main():
    print('#############Olá, bem-vindo ao banco digital PedroPeterPietro###########\n')
    menu = ""

    while(menu != 3):
        print("""
        ############# QUAL AÇÃO VOCÊ DESEJA EXECUTAR? ##################
        1 - Sou Cadastrado
        2 - Cadastrar Usuario
        3 - Sair\n
        """)
        menu = input()
        
        if menu == "1":
            menu_usuario()
        elif menu == "2":
            cadastrar_usuario()
        elif menu == "3":
            break
        elif menu == "admin":
              admin_config()
        else:
              print("Opção incorreta, por favor selecione novamente.\n")

def menu_usuario():
    menu = ""
    usuario_existente = informar_registro()

    if usuario_existente is not None:
        usuario = banco_de_dados[usuario_existente]
        while(menu != 4):
                print("""
                ############# QUAL AÇÃO VOCÊ DESEJA EXECUTAR? ##################
                1 - Sacar
                2 - Depositar
                3 - Visualizar Extrato
                4 - Sair do Menu Usuario\n
                """)
                menu = input()
                
                if menu == "1":
                    sacar(usuario)
                elif menu == "2":
                    depositar(usuario)
                elif menu == "3":
                    verificar_extrato(usuario)
                elif menu == "4":
                    break
                else:
                    print("Opção incorreta, por favor selecione novamente.\n")
    else:
        print("Usuario inexistente, por favor informar o CPF novamente ou fazer o Cadastro na opção 2 - Cadastrar Novo Usuario\n")

def sacar(usuario):

        valor = float(input("Informe o valor do saque: \n"))
        if valor > 0 and valor <= usuario['Saldo']:
            if usuario['Quantidade_de_Saque'] < 3:
                        usuario['Saldo'] -= valor
                        usuario['Extrato'] += f"Saque: R$ {valor:.2f}\n"
                        usuario['Quantidade_de_Saque'] += 1
                        print("Saque Concluido!")
            else:
                        print("Prezado cliente, você já excedeu o limite de saques diários.\n")
        else:
            print("Prezado cliente, o valor digitado é menor que o saldo disponível. Favor tentar novamente.\n")


def depositar(usuario):
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
                    usuario['Saldo'] += valor
                    usuario['Extrato'] += f"Depósito: R$ {valor:.2f}\n"
                    print(f"Depósito Concluido!, o seu saldo atual é igual a R$ {usuario['Saldo']:.2f}")
        else:
                    print("Prezado cliente, o valor digitado não é válido.")

def verificar_extrato(usuario):

    print(f"Esse é o extrato \n{usuario['Extrato']}")


def cadastrar_usuario():
    pos_usuario = 0
    usuario_existente = False
    cpf_valido = False
    global banco_de_dados
    while(usuario_existente != True):
        if f"user{pos_usuario}" in banco_de_dados:
            pos_usuario += 1
        else:
            nome_do_usuario = input("Primeiro, precisamos saber qual o seu nome, poderia inserir por favor?\n")
            data_de_nascimento = input(f"Que Legal! \n Prazer, {nome_do_usuario}, poderia dizer a sua data de nascimento?\n")
            while(cpf_valido == False):
                registro_usuario = input("Agora informe o seu CPF")
                registro_usuario = retornar_apenas_numeros(registro_usuario)
                registro_existente = verificar_registro_existente(registro_usuario)
                if registro_existente:
                    cpf_valido = False
                    print("CPF já existente no nosso Banco de Dados, por favor informe outro CPF.")
                else:
                    cpf_valido = True
            endereco = input('Agora informe por favor o seu endereço. sendo o logradouro - bairro - cidade/sigla estado.\n')
            usuario = {
                'Nome': nome_do_usuario,
                'Data de nascimento': data_de_nascimento,
                "Registro": registro_usuario,
                "Saldo": 0,
                "Extrato": "",
                "Quantidade_de_Saque": 0,
                "Endereço": endereco
            }
            banco_de_dados[f"user{pos_usuario}"] = usuario
            print(f"Usuário {nome_do_usuario} cadastrado com sucesso!")
            usuario_existente = True


def admin_config():
        menu = 0
        senha_geral = input("Olá Administrador, por favor, por medida de segurança pedimos que insira a senha geral \n")
        if senha_geral == "teste":
             while(menu != 4):
                print("""
                ############# QUAL AÇÃO VOCÊ DESEJA EXECUTAR? ##################
                1 - Listar todas as contas cadastradas \n
                """)
                menu = input()
                
                if menu == "1":
                    print(banco_de_dados)
                elif menu == "4":
                      break
                else:
                    print("Opção incorreta, por favor selecione novamente.")
        else:
              print("Senha Incorreta \n")

def retornar_apenas_numeros(string):
      string = re.sub(r'\D', '', string)
      return string

def verificar_registro_existente(registro):
    global banco_de_dados

    for usuario in banco_de_dados.values():
        if usuario['Registro'] == registro:
            return True

    return False

def informar_registro():
    registro_usuario = input("Prezado cliente, primeiro informe o seu CPF para continuarmos a ação \n")
    registro_usuario = retornar_apenas_numeros(registro_usuario)
    for usuario, valores in banco_de_dados.items():
        if 'Registro' in valores and valores['Registro'] == registro_usuario:
            return usuario

    return None



main()

print('Olá, bem-vindo ao banco digital PedroPeterPietro')
menu = ""
quantidade_de_saldo = 0
saldo = 2
extrato = ""

while(menu != 4):
    print("""
    ############# QUAL AÇÃO VOCÊ DESEJA EXECUTAR? ##################
    1 - Sacar
    2 - Depositar
    3 - Visualizar Extrato
    4 - Sair
    """)
    menu = input()
    
    if menu == "1":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0 and valor <= saldo:
            if quantidade_de_saldo < 3:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                quantidade_de_saldo += 1
                print("Saque Concluido!")
            else:
                print("Prezado cliente, você já excedeu o limite de saques diários.")
        else:
            print("Prezado cliente, o valor digitado é menor que o saldo disponível. Favor tentar novamente.")
    
    elif menu == "2":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            quantidade_de_saldo += 1
            print("Depósito Concluido!")
        else:
            print("Prezado cliente, o valor digitado não é válido.")
    
    elif menu == "3":
        print(f"Esse é o extrato {extrato}")

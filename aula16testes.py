import os

while True: 

    print("**Bem Vindo**\n")
    print("1 - Começar")
    print("2 - Sair")
    entrada = input("")

    if entrada == "1" or entrada.lower() == "começar":
        os.system("cls")
        print("Bem vindo ao mundo alternativo")
        break

    elif entrada == "2" or entrada.lower() == "sair":
        os.system("cls")
        print("Você saiu.")
        break
    else:
        os.system("cls")
        print("Erro.")
        print("Digite o número ou o nome de uma das opções.\n")
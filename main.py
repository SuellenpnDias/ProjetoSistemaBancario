# Criação de sistema bancário - versão 1

print("""
      ======== MENU ========
      1. Depósito
      2. Saque
      3. Extrato
      4. Sair

      ======================
      """
      )

deposito = 0
extrato = ""
saldo = 0
LIMITE_SAQUE_DIARIO = 3
limite = 500
numero_de_saques = 0

while True:

    opcao = int(input("Digite o número correspondente a opção desejada:\n \n"))

    if opcao == 1:
        deposito = float(input("Digite o valor que deseja depositar? "))
        if deposito <= 0:
            print("Valor inválido para depósito! Tente novamente")
            print("==============================================")

        else:
            saldo += deposito
            print(
                f"Depósito no valor de R$ {deposito} realizado com sucesso! O valor atual de sua conta é de R$ {saldo}")

            extrato += "\n" + "Depósito no valor de R$ " + str(deposito)


    elif opcao == 2:

        saque = float(input("Digite o valor que deseja sacar? "))

        limite_excedido = saque > limite
        saques_excedidos = numero_de_saques >= LIMITE_SAQUE_DIARIO
        if saque > saldo:
            print("Você não possui saldo suficiente para esta operação!")
            print("====================================================")


        elif saque <= 0:
            print("O valor digitado é inválido!")
            print("============================")



        elif limite_excedido:
            print("Limite de saque atingido!")
            print("=========================")



        elif saques_excedidos:
            print("Você já atingiu o limite diário de saques!")
            print("==========================================")



        else:
            saldo = saldo - saque
            print(f"Saque no valor de R$ {saque} realizado com sucesso!")
            numero_de_saques += 1
            extrato += "\n" + "Saque no valor de R$ " + str(saque)



    elif opcao == 3:
        if extrato == "":
            print("Nenhuma movimentação realizada até o momento!")
            print("==============================================")



        else:
            print("============================")
            print("Confira abaixo seu extrato: ")
            print("============================")
            print(extrato)
            print(f"O saldo atual da conta é R$ {saldo}")
            print("====================================")


    elif opcao == 4:
        print("Você escolheu sair. Até a próxima!")
        break

    else:
        print("Você digitou uma opção inválida! Tente novamente.")
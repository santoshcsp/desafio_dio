menu = '''

[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito no valor de {valor} concluído!")

        else:
            print("Operação não concluída. Informe um valor correto!")        

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = saldo < valor
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Valor do saque excedeu o limite!")

        elif excedeu_saques:
            print("Número de saques diários excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1
            print(f"Saque no valor de {valor} concluído!")

    elif opcao == "e":
        print("Extrato")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

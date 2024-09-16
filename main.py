menubancoEduardo = """"
Selecione a opção desejada:
1 - Depoisito
2 - Saque
3 - Extrato

=> """

saldoConta = 0
limiteConta = 300
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menubancoEduardo)

    if opcao == "1":
        valor = float(input("Digite o valor que quer depositar: "))

    elif opcao == "2":
        valor = float(input("Digite o valor para saque"))

        excedeu_saldo = valor > saldoConta

        excedeu_limite = valor > limiteConta

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sem saldo")

        elif excedeu_limite:
            print("Saque ultrapassa o limite.")

        elif excedeu_saques:
            print("Numero de saques atingidos.")

        elif valor > 0:
            saldoConta -= valor
            numero_saques += 1

        elif opcao == "3":
            print(f"\nSaldo: R$ {saldoConta:.2f}")
            break

        else:
            print("Erro, tente novamente")
    elif opcao == "3":
        print (f"\n Saldo: R${saldoConta:.2f}")

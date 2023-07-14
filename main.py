header = str.center(' Menu ',18,'#')
menu = """

    [d] Depositar
    [s] Saque
    [e] Extrato
    [q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITES_SAQUES = 3
VALOR_SAQUE_LIMITE = 500

while True:
    print(header)
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input())
        if(valor > 0):
            saldo_anterior = saldo
            saldo += valor
            print(f'Valor R$ {valor:.2f} depositado com sucesso. Saldo atual: R$ {saldo:.2f}.')
            extrato.append(f"Deposito: R$ {valor:.2f} | Saldo anterior: {saldo_anterior:.2f} | Saldo atualizado: {saldo:.2f}")
            continue
        
        else:
            print('Operação inválida!')
            continue

    elif opcao == "s":
        valor = float(input())
        if valor > saldo:
            print('Valor para saldo indisponível!')
            continue

        elif numero_saques < LIMITES_SAQUES:
            print('Atigngiu o limites máximo de saques no dia!')
            continue

        elif(valor > 0 and valor <= VALOR_SAQUE_LIMITE):
            saldo_anterior = saldo
            saldo -= valor
            numero_saques += 1
            print(f'Valor R$ {valor:.2f} sacado com sucesso. Saldo atual: R$ {saldo:.2f}.')
            extrato.append(f"Saque: R$ {valor:.2f} | Saldo anterior: {saldo_anterior:.2f} | Saldo atualizado: {saldo:.2f}")
            continue

        else:
            print('Operação inválida!')
            continue

    elif opcao == "e":
        if(len(extrato) > 0):
            for info in extrato:
                print(f"- {info}")

            print(f"Saldo atual: R$ {saldo:.2f}")
            continue

        else:
            print('Não foram realizadas movimentações!')
            continue

    elif opcao == "q":
        print('Sair')
        break

    else:
        print('Error na operação! Tente novamente!')
        continue
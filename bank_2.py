header = str.center(' Menu ',18,'#')
menu = """

    [u] Criar usuário
    [l] Listar usuários
    [c] Criar Conta
    [d] Depositar
    [s] Saque
    [e] Extrato
    [q] Sair

"""

saldo = 0
limite = 500
extrato = []
usuarios = []
contas = []
numero_saques = 0
LIMITES_SAQUES = 3
VALOR_SAQUE_LIMITE = 500

def deposito(valor, saldo, /):
    if(valor > 0):
        saldo_anterior = saldo
        saldo += valor
        print(f'Valor R$ {valor:.2f} depositado com sucesso. Saldo atual: R$ {saldo:.2f}.')
        extrato.append(f"Deposito: R$ {valor:.2f} | Saldo anterior: {saldo_anterior:.2f} | Saldo atualizado: {saldo:.2f}")
        return [saldo, extrato]
    else:
        print('Operação inválida!')

def saque(*,valor, saldo, extrato, limite, numero_saques, limites_saques):
    if valor > saldo:
        print('Valor para saldo indisponível!')

    elif numero_saques < LIMITES_SAQUES:
        print('Atigngiu o limites máximo de saques no dia!')

    elif(valor > 0 and valor <= VALOR_SAQUE_LIMITE):
        saldo_anterior = saldo
        saldo -= valor
        numero_saques += 1
        print(f'Valor R$ {valor:.2f} sacado com sucesso. Saldo atual: R$ {saldo:.2f}.')
        extrato.append(f"Saque: R$ {valor:.2f} | Saldo anterior: {saldo_anterior:.2f} | Saldo atualizado: {saldo:.2f}")
        return [saldo, extrato]

    else:
        print('Operação inválida!')

def print_extrato(saldo,/, *, extrato):
    if(len(extrato) > 0):
        for info in extrato:
            print(f"- {info}")

        print(f"Saldo atual: R$ {saldo:.2f}")

    else:
        print('Não foram realizadas movimentações!')

def usuario_existe(cpf, list_usuarios):
    for i in list_usuarios:
        if cpf in i:
            return True
        else:
            return False
        
def criar_usuario(nome, data_de_nascimeto, cpf, endereco, usuarios):
    if not usuario_existe(cpf, usuarios):
        
        usuarios.append({cpf : {'nome': nome, 'data_de_nascimeto': data_de_nascimeto, 'endereco': endereco}})
        print(f"Usuário cadastrado: {usuarios}")

    else:
        print('Usuário já está cadastrado')

def criar_conta(cpf, usuarios, contas):
    if usuario_existe(cpf, usuarios):
        id = len(contas)
        agencia = '0001'
        contas.append({'conta': id, 'agencia' : agencia, 'cpf': cpf})
        print(contas)

    else:
        print('Nenhum Usuário cadastrado com o CPF informado')
    
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario)

while True:
    print(header)
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input())
        deposito(valor, saldo)
        continue

    elif opcao == "s":
        valor = float(input())
        saque(valor=valor,saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limites_saques=LIMITES_SAQUES)
        continue
        
    elif opcao == "e":
        print_extrato(saldo, extrato=extrato)
        continue

    elif opcao == 'u':
        nome = input('Informe o nome:')
        data_de_nascimeto= input('Informe a data de nascimento:')
        cpf= input('Informe o CPF:')
        endereco = input('Informe o endereco:')
        criar_usuario(nome, data_de_nascimeto, cpf, endereco, usuarios)
        continue

    elif opcao == 'l':
        listar_usuarios(usuarios)
        continue

    elif opcao == 'c':
        cpf= input('Informe o CPF:')
        criar_conta(cpf, usuarios, contas)
        continue

    elif opcao == "q":
        print('Sair')
        break

    else:
        print('Error na operação! Tente novamente!')
        continue
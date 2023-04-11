#Sistema Bancário 02
from datetime import datetime

def principal():
    data = datetime.today().date()
    numero_saques = 0
    saldo = 0
    extrato = ''
    LIMITE_VALOR_SAQUE = 500
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == 1:
            print(f'{"--" * 20}\n{"DEPOSITO":^40}')
            valor = int(input('Qual o valor do deposito? R$: '))

            saldo, extrato, data = deposito(saldo, valor, extrato, data)

        elif opcao == 2:
            print(f'{"--" * 20}\n{"SAQUE":^40}')
            valor = int(input('Qual o valor do saque? R$: '))

            saldo, extrato, data, numero_saques = saque(saldo=saldo, extrato=extrato, data=data, LIMITE_VALOR_SAQUE=LIMITE_VALOR_SAQUE, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, valor=valor)

        elif opcao == 3:
            print(f'{"--" * 20}\n{"EXTRATO":^40}')
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            print(f'{"--" * 20}\n{"NOVA CONTA":^40}')
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 5:
            print(f'{"--" * 20}\n{"LISTAR CONTAS":^40}')
            listar_contas(contas)

        elif opcao == 6:
            print(f'{"--" * 20}\n{"NOVO CLIENTE":^40}')
            cadastrar_cliente(clientes)

        elif opcao == 7:
            print(f'{"--" * 20}')
            print('Você selecionou a opção sair, por isso estamos encerrando o sistema.')
            break

        else:
            print('Opção inválida! Digite o número de uma opção válida.')

def menu():
    print(
        f'{"--" * 20}\n'
        f'{"  Esse é o seu MENU DE OPÇÕES"}\n'
        f'{"     [ 1 ] DEPOSITO"}\n'
        f'{"     [ 2 ] SAQUE"}\n'
        f'{"     [ 3 ] EXTRATO"}\n'
        f'{"     [ 4 ] NOVA CONTA"}\n'
        f'{"     [ 5 ] LISTAR CONTAS"}\n'
        f'{"     [ 6 ] NOVO CLIENTE"}\n'
        f'{"     [ 7 ] SAIR"}\n'
        f'{"--" * 20}')
    opcao = int(input('Digite o número de uma opção: '))
    return opcao

def deposito(saldo, valor, extrato, data, /):
    if valor > 0:
        print(f'O deposito no valor de R${valor:.2f} reais, foi efetuado com sucesso!')
        saldo += valor
        extrato += f'Deposito - {data} - R$:{valor:.2f}\n'
    else:
        print('O valor do deposito digitado é inválido. Escolha novamene a opção.')

    return saldo, extrato, data


def saque(*, saldo, extrato, data, LIMITE_VALOR_SAQUE, numero_saques, LIMITE_SAQUES, valor):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE_VALOR_SAQUE
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('O saque não foi realizado pois excedeu o valor total do saldo.')
    elif excedeu_limite:
        print(
            'O limite para saques é R$500.00 reais, o valor solicitado é maior do que o limite. Portanto o saque não foi realizado.')
    elif excedeu_saques:
        print(
            'A quantidade máxima de saques realizados em um dia são 3. Esse saque não pode ser realizado pois já atingiu o limite de saques para hoje.')
    elif 0 < valor <= 500:
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque    - {data} - R$:{valor:.2f}\n'
        print(f'O saque no valor de R${valor:.2f} reais, foi realizado com sucesso')
    else:
        print('O valor do saque solicitado é inválido. Escolha novamente a opção.')

    return saldo, extrato, data, numero_saques


def mostrar_extrato(saldo, /, *, extrato):

    if not extrato:
        print('Não foi realizada nenhuma transação.')
        print(f'O saldo da conta é R${saldo:.2f} reais.')
    else:
        print(extrato)
        print(f'O saldo da conta é R${saldo:.2f} reais.')


def cadastrar_cliente(clientes):
    cpf = str(input('Qual o número do CPF do novo cliente? Digite apenas os números: '))
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('Novo cliente não cadastrado. Já existe um cliente com esse CPF!')
        return

    nome = str(input('Qual o nome completo do novo cliente? '))
    data_nascimento = str(input('Qual a data de nascimento do novo cliente? Digite dd-mm-aaaa: '))
    endereco = str(input('Qual o endereço do novo cliente? Digite logradouro, número - bairro - cidade/sigla do estado e CEP: '))
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('Novo cliente cadastrado com sucesso!')

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = str(input('Qual o número do CPF do novo cliente? Digite apenas os números: '))
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('A nova conta foi criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print('Cliente não encontrado na nossa lista de clientes! É necessário cadastrar o cliente para conseguir criar a nova conta.')

def listar_contas(contas):
    for conta in contas:
        print(f'{"**" * 20}\n'
        f'{"Agência: "}{conta["agencia"]}\n'
        f'{"C/c: "}{conta["numero_conta"]}\n'
        f'{"Cliente: "}{conta["cliente"]}')
        print(f'{"**" * 20}\n')

principal()
#Sistema Bancário
import datetime

data = datetime.datetime.today().date()
numero_saques = 0
saldo = 0
extrato = ''
LIMITE_VALOR_SAQUE = 500
LIMITE_SAQUES = 3
print(f'{"--" * 20}\n{"SEJA BEM VINDO AO NOSSO BANCO":^40}')

while True:
    menu = print(f'{"--" * 20}\n{"  Esse é o seu MENU DE OPÇÕES"}\n{"     [ 1 ] DEPOSITO"}\n{"     [ 2 ] SAQUE"}\n{"     [ 3 ] EXTRATO"}\n{"     [ 4 ] SAIR"}\n{"--" * 20}')
    opção = int(input('Digite o número de uma opção: '))
    if opção == 1:
        print(f'{"--" * 20}\n{"DEPOSITO":^40}')
        valor_deposito = int(input('Qual o valor do deposito? R$: '))
        if valor_deposito > 0:
            print(f'O deposito no valor de R${valor_deposito:.2f} reais, foi efetuado com sucesso!')
            saldo += valor_deposito
            extrato += f'Deposito - {data} - R$:{valor_deposito:.2f}\n'
        else:
            print('O valor do deposito digitado é inválido. Escolha novamene a opção.')

    elif opção == 2:
        print(f'{"--" * 20}\n{"SAQUE":^40}')
        valor_saque = int(input('Qual o valor do saque? R$: '))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > LIMITE_VALOR_SAQUE
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print('O saque não foi realizado pois excedeu o valor total do saldo.')
        elif excedeu_limite:
            print('O limite para saques é R$500.00 reais, o valor solicitado é maior do que o limite. Portanto o saque não foi realizado.')
        elif excedeu_saques:
            print('A quantidade máxima de saques realizados em um dia são 3. Esse saque não pode ser realizado pois já atingiu o limite de saques para hoje.')
        elif 0 < valor_saque <= 500:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'Saque    - {data} - R$:{valor_saque:.2f}\n'
            print(f'O saque no valor de R${valor_saque:.2f} reais, foi realizado com sucesso')
        else:
            print('O valor do saque solicitado é inválido. Escolha novamente a opção.')

    elif opção == 3:
        print(f'{"--" * 20}\n{"EXTRATO":^40}')
        if not extrato:
            print('Não foi realizada nenhuma transação.')
            print(f'O saldo da conta é R${saldo:.2f} reais.')
        else:
            print(extrato)
            print(f'O saldo da conta é R${saldo:.2f} reais.')

    elif opção == 4:
        print(f'{"--" * 20}')
        print('Você selecionou a opção sair, por isso estamos encerrando o sistema.')
        break
    else:
        print('Opção inválida! Digite o número de uma opção válida.')
        

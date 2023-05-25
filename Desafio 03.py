from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.saque(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self):
        self._transacoes.append(f'Tipo: {transacao.__class__.__name__}'
                                f'Valor: {trasacao.valor}'
                                f'data: {datetime.today().day:02}-{datetime.today().month:02}-{datetime.today().year} - {datetime.today().hour:02}:{datetime.today().minute:02}:{datetime.today().second:02}')


class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def saque(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('O saque não foi realizado pois excedeu o valor total do saldo.')

        elif 0 < valor <= 500:
            self._saldo -= valor
            print(f'O saque no valor de R${valor:.2f} reais, foi realizado com sucesso')
            return True

        else:
            print('O valor do saque solicitado é inválido. Operação não realizada.')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'O deposito no valor de R${valor:.2f} reais, foi efetuado com sucesso!')
            return True
        else:
            print('O valor do deposito digitado é inválido. Escolha novamene a opção.')
            return False


class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite_valor=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite_valor = limite_valor
        self.limite_saques = limite_saques

    def saque(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite_valor = valor > self.limite_valor
        excedeu_limite_saques = numero_saques > self.limite_saques

        if excedeu_limite_valor:
            print('O limite para saques é R$500.00 reais, o valor solicitado é maior do que o limite. Portanto o saque não foi realizado.')

        elif excedeu_saques:
            print('A quantidade máxima de saques realizados em um dia são 3. Esse saque não pode ser realizado pois já atingiu o limite de saques para hoje.')

        else:
            return super().saque(valor)

        return False

    def __str__(self):
        print(f'{"**" * 20}\n'
              f'{"Agência: "}{self.agencia}\n'
              f'{"C/c: "}{self.numero}\n'
              f'{"Cliente: "}{self.cliente.nome}')
        print(f'{"**" * 20}\n')


class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


class Pessoa_Fisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento




principal()
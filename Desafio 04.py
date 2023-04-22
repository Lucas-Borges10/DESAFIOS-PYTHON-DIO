import sqlalchemy as sqLA
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine
from sqlalchemy import Integer, select
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import inspect

Base = declarative_base()

class Cliente(Base):

   __tablename__ = "conta_cliente"
   sobrenome_completo = Column(String)
   id = Column(Integer, primary_key=True)
   nome = Column(String)
   cpf = Column(String(9))
   endereco = Column(String)

   conta = relationship(
       "Conta", back_populates='cliente'
   )

   def __repr__(self):
       return f'Cliente(id={self.id}, nome={self.nome}, sobrenome_completo={self.sobrenome_completo}, cpf={self.cpf}'


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    agencia = Column(String)
    numero = Column(Integer)
    id_cliente = Column(Integer, ForeignKey('conta_cliente.id'), nullable=False)
    saldo = Column(String)

    cliente = relationship("Cliente", back_populates='conta')

    def __repr__(self):
        return f'Conta(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, numero={self.numero}, id_cliente{self.id_cliente}, saldo={self.saldo}'


print(Cliente.__tablename__)
print(Conta.__tablename__)

engine = create_engine('sqlite://')

Base.metadata.create_all(engine)

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table('conta_cliente'))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as sessao:

    joao = Cliente(
        nome='João',
        sobrenome_completo='João Antunes',
        cpf='123456789',
        endereco='Av. Pedro Ludovico',
        conta=[Conta(tipo='corrente',
                     agencia='0001',
                     numero=12345,
                     saldo='1999,20')
               ]
    )

    ana = Cliente(
        nome='Ana',
        sobrenome_completo='Ana Maria',
        cpf='987654321',
        endereco='Av. 15 de Novembro',
    conta = [Conta(tipo='corrente',
                   agencia='0001',
                   numero=56789,
                   saldo='100')]
    )

    joaquim = Cliente(
        nome='Joaquim',
        sobrenome_completo='Joaquim Emanuel',
        cpf='147258369',
        endereco='Av. 24 de Maio',
    conta = [Conta(tipo='corrente',
                   agencia='0001',
                   numero=14752,
                   saldo='0')]
    )

    sessao.add_all([joao, ana, joaquim])
    sessao.commit()

stmt = select(Cliente).where(Cliente.nome.in_(['João', 'Joaquim']))
print('\nRecuperando usuários filtrados')
for cliente in sessao.scalars(stmt):
    print(cliente)

stmt_conta = select(Conta).where(Conta.id_cliente.in_([2]))
print('\nRecuperando conta de Ana')
for conta in sessao.scalars(stmt_conta):
    print(conta)

stmt_ordem = select(Cliente).where(Cliente.id)
print('\nRecuperando informações de maneira ordenada')
for resultado in sessao.scalars(stmt_ordem):
    print(resultado)

stmt_junto = select(Cliente).where(Cliente.id, Conta.numero).join_from(Cliente, Conta)
print('\n')
for resultado in sessao.scalars(stmt_junto):
    print(resultado)

coneccao = engine.connect()
resultados = coneccao.execute(stmt_junto).fetchall()
print('\nExecutando a partir da conecção')
for resultado in resultados:
    print(resultado)

stmt_contas = select(func.count('*')).select_from(Cliente)
print('\nTotal de instâncias em Cliente')
for resultado in sessao.scarlars(stmt_contas):
    print(resultado)


print('Encerrando a sessão.')
session.close()

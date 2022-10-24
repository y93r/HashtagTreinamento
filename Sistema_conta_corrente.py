from datetime import datetime
from msilib.schema import SelfReg
from re import S
import pytz
from random import randint

class ContaCorrente:
    
    @staticmethod
    def _data_hora(): 
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y  %H:%M:%S')

    def __init__(self, nome, cpf, agencia,num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []

    
    def consultar_saldo(self):
        print('Seu saldo atual é de R$ {:,.2f}.'.format(self.saldo))

    def depositar(self,valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor!')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
    
    def consultar_lim_chequespcial(self):
        print('Seu limite de cheque especial é de R$ {:,.2f}.'.format(self._limite_conta()))

    def consultar_historico(self):
        print('HISTORICO DE TRANSAÇÕES')
        print('Valor, Saldo, Data E Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self,valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora(): 
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.val = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year +5)
        self.cod_seg = '{}{}{}'.format(randint (0,9), randint (0,9), randint (0,9))
        self.lim = 1000
        self._senha = ''
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self,valor):
        if len(valor) ==4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha inválida.')

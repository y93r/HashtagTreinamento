from random import randint

class Agencia:
    def __init__(self,tel, cnpj,num):
        self.tel = tel
        self.cnpj = cnpj
        self.num = num
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_cx(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: R$ {:,.2f}'.format(self.caixa))
        else:
            print('O valor de caixa está OK. Caixa atual: R$ {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível no caixa.')

    def add_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

class AgenciaVirtual (Agencia):
    def __init__(self, site, tel, cnpj):
        self.site = site 
        super().__init__(tel, cnpj, 1000)
        self.caixa = 1000000
        self.cx_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.cx_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa -= valor
        self.cx_paypal += valor
        

class AgenciaComum (Agencia):
    def __init__(self, tel, cnpj): 
        super().__init__(tel, cnpj, num=randint(1001,9999))
        self.caixa = 1000000

class AgenciaPremium (Agencia):
    def __init__(self, tel, cnpj): 
        super().__init__(tel, cnpj, num=randint(1001,9999))
        self.caixa = 10000000

    def add_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().add_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimônio minímo necessário para entrar na Agência Premium!')

if __name__ == '__main__':

#programa
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com', 45697841, 4444888803)
    agencia_virtual.verificar_cx()

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.cx_paypal)

    agencia_premium = AgenciaPremium(98740212, 3333888803)
    #agencia_premium.verificar_cx()

    agencia_premium.add_cliente('Yara', 12345678903, 25000)
    print(agencia_premium.clientes)

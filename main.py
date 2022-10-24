from Sistema_conta_corrente import ContaCorrente, CartaoCredito
from Agencia import Agencia, AgenciaComum, AgenciaPremium, AgenciaVirtual

#programa
conta_Yara = ContaCorrente('Yara', '123.456.789-01', '1234', '333999')
conta_Yara.consultar_saldo()

#fazendo depósito
conta_Yara.depositar(5000)
conta_Yara.consultar_saldo()

#sacando dinheiro
conta_Yara.sacar_dinheiro(500)

print('\n Saldo final')
conta_Yara.consultar_saldo()
conta_Yara.consultar_lim_chequespcial()

#print('='*30)
#conta_Yara.consultar_historico()

print('='*30)
conta_Mayara = ContaCorrente('Mayara', "987.654.321-06", '9874', '505030')
conta_Yara.transferir (100, conta_Mayara)

conta_Yara.consultar_saldo()
conta_Mayara.consultar_historico()

print('='*30)
conta_Yara.consultar_historico()

print('='*30)
conta_Mayara.consultar_historico()

cartao_Yara = CartaoCredito('Yara', conta_Yara)
print(cartao_Yara.conta_corrente.num_conta)
print(cartao_Yara.numero)
print(cartao_Yara.cod_seg)
print(cartao_Yara.val)

#consultar 
print(conta_Yara.__dict__)
print(cartao_Yara.__dict__)
print('OLÁ SEJA BEM VINDO A NOSSA LOJA !!!')
v = float(input('Digite o valor da sua compra: '))
print('[1] Á vista dinheiro/cheque: 10% de desconto')
print('[2] Á vista no cartão: 5% de desconto')
print('[3] Em até 2x no cartão: preço normal')
print('[4] 3x ou mais no cartão: 20% de juros')
e = int(input('Digite o NÚMERO da opção de pagamento: '))
if e == 1:
    r1 = v-(v / 10)
    print('O valor a ser pago é igual á {} reais'.format(r1))
elif e == 2:
    r2 = v-(v/20)
    print('O valor a ser pago é igual á {} reais'.format(r2))
elif e == 3:
    r3 = v / 2
    print('O valor a ser pago é igual á 2x {} reais'.format(r3))
elif e == 4:
    r4 = v + (v / 5)
    print('O valor total a ser pago é igual á {} rais, dividido em até 12 parcelas'.format(r4))
    np = int(input('Em quantas parcelas você deseja fazer: '))
    print('O seu pagamento vai ser dê: {} reais por {} meses'.format(r4/np, np))

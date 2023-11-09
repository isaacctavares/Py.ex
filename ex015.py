dias = float(input('Quantos dias você ficou com o carro: '))
km = float(input('Quantos km você andou com ele: '))
vd = dias * 60
vkm = km * 0.15
vt = vd + vkm
print('O valor total do aluguel desse carro é igual á: {} reais'.format(vt))
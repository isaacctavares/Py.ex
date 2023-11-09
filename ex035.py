print('=-=' * 20)
r1 = float(input('Digite o valor de uma seguimento de reta: '))
r2 = float(input('Digite o valor de uma seguimento de reta: '))
r3 = float(input('Digite o valor de uma seguimento de reta: '))
print('=-=' * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print('Os seguimentos {}, {}, {} conseguem formar um treiâgulo!'.format(r1, r2, r3))
else:
    print('Os seguimentos {}, {}, {} não conseguem formar um triângulo!'.format(r1, r2, r3))
n = int(input('Digite um numero:'))
u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10
print('Analisando esse número...')
print('Unidade: {}'.format(u))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Milhar: {}'.format(m))
d = float(input('Qual a distancia em km da sua viagem? '))
print('Você está prestes a começar uma viagem de {} km'.format(d))
if d <= 200:
    print('O valor da sua viagem é de {} reais'.format(d * 0.5))
else:
    d > 200
    print('O valor da sua viagem será de {} reais'.format(d * 0.45))


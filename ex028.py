import random
print('Vou pensar em um número de 0 a 5')
n = int(input('Tente adivinhar qual número de 0 a 5 eu escolhi: '))
lista = [0, 1, 2, 3, 4, 5]
ne = random.choice(lista)
print('PROCESSANDO')
if n == ne:
    print('Você acertou o número que escolhi!')
else:
    print('Você errou o número que escolhi!')



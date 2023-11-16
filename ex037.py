import math
n = int(input('Escreva um número inteiro qualquer: '))
print('Digite 1 se for para base numeria binaria')
print('Digite 2 se for para a base numerica octal')
print('Digite 3 se for para base numerica hexadecimal')
b = int(input('Qual base numerica você quer converte-lo: '))
if b == 1:
    print('Seu número em base Binária é igual á {}'.format(bin(n)))
elif b == 2:
    print('Seu número em base numerica octal é igual á {}'.format(oct(n)))
elif b == 3:
    print('Seu número em base numerica hexadecimal é igual á {}'.format(hex(n)))
else:
    print('\033[1;31mnúmero selecionado não correseponde a nenhuma base numerica :(\033[m')
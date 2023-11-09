a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c: int = int(input('Terceiro número: '))
# VERIFICANDO QUEM É O MENOS:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# VERIFICANDO QUEM É O MAIOR:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é: {}'.format(menor))
print('O maior número é: {}'.format(maior))

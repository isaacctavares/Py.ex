import random
p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
l = [p1, p2, p3, p4]
random.shuffle(l)
print('A ordem de apresentação será: ')
print(l)
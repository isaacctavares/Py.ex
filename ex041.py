from datetime import date
ano = float(input('Informe a sua data de nescimento: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Você tem {} anos'.format(idade))
    print('A sua categoria é considerada MIRIM')
elif idade > 9 and idade <= 14:
    print('Você tem {} anos'.format(idade))
    print('A sua categoria é INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você tem {} anos'.format(idade))
    print('A sua categoria é JÚNIOR')
elif idade > 19 and idade <= 25:
    print('Você tem {} anos'.format(idade))
    print('A sua categoria é SÊNIOR')
elif idade > 25:
    print('Você tem {} anos'.format(idade))
    print('A sua categoria é MASTER')

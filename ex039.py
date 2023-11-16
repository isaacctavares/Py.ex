from datetime import date
atual = date.today().year
ano = int(input('Qual a sua data de nascimento? '))
idade = (atual - ano)
print('A sua idade é igual á {}'.format(idade))
if idade < 18:
    print('Você ainda vai se alistar!!!')
    saldo = ano + 18
    print('Você deve se alistado em {}'.format(saldo))
elif idade == 18:
    print('Está no ano de alistamento ao serviço militar!!!')
elif idade > 18:
    print('Já se passou a idade sua de alistamneto!!!')
    saldo = ano + 18
    print('Você deveria ter se alistado em {}'.format(saldo))

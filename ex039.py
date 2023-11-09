ano = int(input('Qual a sua data de nascimento? '))
idade = (2023 - ano)
if idade < 18:
    print('Você ainda vai se alistar!!!')
elif idade == 18:
    print('Está no ano de alistamento ao serviço militar!!!')
elif idade < 18:
    print('Ainda não está no seu ano de alistamento militar obrigatorio!!!')
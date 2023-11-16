n1 = float(input('Digite a sua nota do primeiro bimestre: '))
n2 = float(input('Digite a sua nota do segundo bimestre: '))
n3 = float(input('Digite a sua nota do terceiro bimestre: '))
n4 = float(input('Digite a sua nota do quarto bimestre: '))
m = (n1+n2+n3+n4)/4
if m > 7:
    print('sua média anual foi dê: {}'.format(m))
    print('\033[1;32mvocê foi aprovado!!!\033[m')
elif m < 4.9:
    print('sua média anual foi dê: {}'.format(m))
    print('\033[1;31mvocê foi reprovado!!!\033[m')
elif m > 4.9 and m < 7:
    print('sua média anual foi dê: {}'.format(m))
    print('\033[1;33mvocê está de recuperação!!!\033[m')

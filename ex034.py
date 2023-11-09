s = float(input('Qual é o salário do funcionario: R$'))
if s <= 1250:
    sf = ((s/100) * 15) + s
    print('O salario desse funcionario passou de R${} para R${}'.format(s, sf))
else:
    s >= 1250
    sf1 = ((s/100) * 10) + s
    print('O salario desse funcionario passou de R${} para R${}'.format(s, sf1))

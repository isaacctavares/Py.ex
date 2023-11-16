ve = float(input('Qual o valor do emprestimo: R$'))
s = float(input('Qual o valor do seu salario mensal: R$'))
t = int(input('Qual o tempo desejado para pagar o emprestimo em anos: '))
r = ve / (t * 12)
vp = (r * 0.13) + r
if r < (s / 100) * 30:
    print('\033[1;33mAnalisando a sua situação...\033[m')
    print('\033[1;32mFoi aprovado o seu emprestimo!!!\033[m')
    print('O valor da sua parcela mensal será de R${:.2f}'.format(vp))
elif r > (s / 100) * 30:
    print('\033[1;33mAnalisando a sua situação...\033[m')
    print('\033[1;31mFoi negado o seu emprestimo pois a parcela mensal excedeu 30% do seu salario mensal :(\033[m')

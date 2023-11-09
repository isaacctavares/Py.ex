v = float(input('Digite a velocidade em que o carro passou no radar: '))
if v > 80:
    print('Você foi multado por excesso de velocidade! :(')
    print('O valor da sua multa é de {} reais'.format(((v) - 80)*7))
else:
    print('Você passou no limite adequado para via :)')
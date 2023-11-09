na = float(input('Digite um numero inteiro: '))
nb = float(input('Digite mais um númro inteiro: '))
if na > nb:
    print('O número maior é {} e o menor {}'. format(na, nb))
elif nb > na:
    print('O numero maior é {} e o menor {}'.format(nb, na))
elif na == nb:
    print('Os numero são iguais!!!')
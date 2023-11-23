import random
from time import sleep
print('\033[1;32mVAMOS JOGAR PEDRA, PAPEL E TESOURA\033[m')
print('Escolha uma das opções')
pedra = print('[1] PEDRA')
papel = print('[2] PAPEL')
tesoura = print('[3] TESOURA')
e = int(input('Escolha qual você quer: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')
sleep(1)
l = [1, 2, 3]
em = random.choice(l)
if e == 1 and em == 2:
    print('\033[1;31mVocê perdeu o computador escolheu PAPEL')
elif e == 2 and em == 1:
    print('\033[1;32mVocê ganhou !! O computador escolheu PEDRA')
elif e == 2 and em == 3:
    print('\033[1;31mVocê perdeu o computador escolheu TESOURA\033[m')
elif e == 3 and em == 2:
    print('\033[1;32mVocê ganhou !! O computador escolheu PAPEL')
elif e == 1 and em == 3:
    print('\033[1;32mVocê ganhou !! O computador escolheu TESOURA')
elif e == 3 and em == 1:
    print('\033[1;31mVocê perdeu o computador escolheu PEDRA\033[m')
elif e == em:
    print('\033[1;33mFICOU EMPATADO !!! O COMPUTADOR ESCOLHEU O MESMO QUE VOCÊ')
else:
    print('\033[1;35mJOGADA INVALIDA')
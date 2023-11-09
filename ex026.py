n = str(input('Digite algo: ')).upper().strip()
print('O número de letras "a" no seu nome é {}'.format(n.count('A')))
print('A primeira letra "a" aparece na posição {}'.format(n.find('A') + 1))
print('A última letra "a" aparece na posição {}'.format(n.rfind('A')))
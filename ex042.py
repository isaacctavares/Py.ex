print('Digite os sgmentos do seu triâmgulo')
n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n2 + n1:
    print('O seu segmentos podem formar um triângulo')
    if n1 == n2 == n3:
        print('Os seus segmentos formam um triângulo EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('Os seus segmentos formam um triângulo ESCALENDO')
    else:
        print('Os seus segmentos formam um triângulo ISÓSCELES')
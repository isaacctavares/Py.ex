print('\033[1;32mOLÁ VAMOS VER COMO ESTÁ O SEU INDÍCE DE MASSA CORPORAL?\033[m')
p = float(input('Digíte seu peso corporal em KG: '))
h = float(input('Digite sua altura em metros: '))
imc = p / (h*h)
print("seu IMC é dê: {:.2f}".format(imc))
if imc < 18.5:
    print('\033[1;31mVocê está abaixo do peso\033[m')
elif imc > 18.5 and imc < 24.9:
    print('\033[1;32mVocê esta no peso normal\033[m')
elif imc > 24.9 and imc < 29.9:
    print('\033[1;33mVocê está em sobrepeso\033[m')
elif imc > 29.9 and imc < 34.9:
    print('\033[1;31mVocê está em obesidade classe I\033[m')

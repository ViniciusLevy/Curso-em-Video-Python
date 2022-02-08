peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO! Vai comer alguma coisa meio quilo!!!')
elif 18.5 <= imc <= 25:
    print('PESO IDEAL! Hmmmmmmmmm!!!')
elif 25 < imc <= 30:
    print('SOBREPESO! Melhor dar uma segurada no lanchinho!')
elif 30 < imc <= 40:
    print('OBESIDADE! Caralho!!! Para de comer Demônioooo!!!!!')
else:
    print('OBESIDADE MÓRBIDA! Você vai MORRERRRRRRR!!!!')
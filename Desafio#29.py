kmh = float(input('Qual a velocidade do veículo? '))
if kmh > 80:
    multa = (kmh - 80)*7
    print('Você passou do limite de velocidade de 80 km/h, sua multa será de R$ {:.2f}.'.format(multa))
else:
    print('Você está dentro do limite de 80 km/h.')

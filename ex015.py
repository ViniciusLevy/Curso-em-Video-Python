km_percorrido = float(input('Informe a kilometragem: '))
dias_de_aluguel = int(input('Informe a quantidade de dias de alguel do carro: '))
alguel_total = (km_percorrido * 0.15) + (dias_de_aluguel * 60.00)
print('Foram percorridos {:.2f} km e o carro permaceu alugado por {} dias, totalizando um aluguel de R${:.2f}.'.format(km_percorrido, dias_de_aluguel, alguel_total))


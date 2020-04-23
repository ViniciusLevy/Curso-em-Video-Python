altura = float(input('Insira a altura da parede que deseja pintar: '))
largura = float(input('Insira a largura da parade que deja pintar: '))
area = altura * largura
tinta = area / 2
# 1 lata de tinta faz o equivalente a 2m².
print('Você precisa pintar uma área de {} m², para isso, será necessário {} litros de tinta.'.format(area, tinta))

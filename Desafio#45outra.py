from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-=' * 8)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('=-=' * 8)
if computador == jogador:
    print('EMPATE!')
elif computador == 0 and jogador == 1:
    print('JOGADOR VENCE!')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCE!')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCE!')
elif computador == 1 and jogador == 2:
    print('JOGADOR VENCE!')
elif computador == 2 and jogador == 0:
    print('JOGADOR VENCE!')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENDE!')

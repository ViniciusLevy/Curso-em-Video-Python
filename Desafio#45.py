from random import randint
from time import sleep
print(''''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-=' * 8)
# definição de jogada do computador
if computador == 0:
    print('Computador jogou Pedra')
elif computador == 1:
    print('Computador jogou Papel')
elif computador == 2:
    print('Computador jogou Tesoura')
# definição de jogada do jogador
if jogador == 0:
    print('Jogador jogou Pedra')
elif jogador == 1:
    print('jogador jogou Papel')
elif jogador == 2:
    print('Jogador jogou Tesoura')
else:
    print('TENTE NOVAMENTE! ESCOLHA UMA DAS OPÇÕES INDICADAS.')
print('=-=' * 8)
# possíveis placares
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

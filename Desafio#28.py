import random
from time import sleep
num = random.randrange(0, 5)
print('-=-' * 20)
print('Vou pensar em um número, quero ver você adivinhar!!!')
print('-=-' * 20)
pergunta = int(input('Qual número pensei? '))
print('PROCESSANDO...')
sleep(3)
if pergunta == num:
    print('Parabéns, você acertou o número!!!')
else:
    print('NÃOOOOO, LOSERRRRRR!!!!')

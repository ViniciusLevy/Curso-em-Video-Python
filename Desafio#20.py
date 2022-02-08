'''from random import sample
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

ordem = sample([aluno1, aluno2,aluno3, aluno4], k=4)

print('A lista de alunos sorteada é :{}'.format(ordem))'''

from random import shuffle
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

ordem = [aluno1, aluno2,aluno3, aluno4]

shuffle(ordem)

print('A lista de alunos sorteada é :{}')
print(ordem)


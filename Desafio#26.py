frase = str(input('Escreva uma frase: ')).upper().strip()
print('A letra A aparece na frase {} vezes.'.format(frase.count('A')))
print('A primeira letra A apraceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))

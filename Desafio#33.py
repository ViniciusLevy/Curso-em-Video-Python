n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1 > n2:
    maior = n1
else:
    maior = n2
if maior > n3:
    print('O maior número é {:.2f}.'.format(maior))
else:
    print('O maior número é {:.2f}.'.format(n3))
if n1 == n2 or n2 == n3 or n1 == n3:
    print('Temos número iguais.')


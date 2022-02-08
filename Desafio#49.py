num = int(input('Digite um número para ver a tabuada: '))
for n in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(num, n, num*n))
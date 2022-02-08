num = int(input('Digite um múmero para análise: '))
div = num % 2
if div == 0:
    print('O número {:.0f} é par!'.format(num))
else:
    print('O número {:.0f} é impar!'.format(num))

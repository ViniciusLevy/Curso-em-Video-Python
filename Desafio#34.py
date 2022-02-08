salario = float(input('Informe seu salário: '))
if salario > 1250.00:
    print('O rejuste para seu salário é de 10%, totalizando o valor de R$ {:.2f}.'.format(salario * 1.1))
else:
    print('O reajuste para seu salário é de 15%, totalizando o valor de R$ {:.2f}. '.format(salario * 1.15))

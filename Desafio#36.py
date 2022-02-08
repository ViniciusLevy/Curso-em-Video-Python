valor_do_imovel = float(input('Digite o valor do imóvel que quer comprar: '))
salario = float(input('Qual o valor do seu salário mensal: '))
anos_pagamento = int(input('Em quantos anos vai realizar o pagamento: '))

prestacao = valor_do_imovel / (anos_pagamento * 12)  # calcula o valor da prestação.

print(' ')
print('Obrigado por simular o empréstimo conosco!')
print('O valor do imóvel simulado é: R$ {:.2f}. '
      '\nO Salário informado é de R$ {:.2f}. '
      '\nSerá pago em {:.0f} anos.'.format(valor_do_imovel, salario, anos_pagamento))
print(' ')

if prestacao > salario * 0.30:  # Calcula se o valor é superior a 30% do salário, caso seja, será negado.
    print('\33[1;31mNEGADO!\33[m O valor da prestação é superior a 30% do seu salário.')
else:
    print('\33[1;32mPARABÉNS!!!\33[m Seu empréstimo foi aprovado!')

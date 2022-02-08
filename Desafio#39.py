from datetime import date
atual = date.today().year
sexo = str(input('Qual o seu sexo? ')).strip().upper()
if sexo == 'MASCULINO':
    nascimento = int(input('Qual o ano do seu nascimento? '))
    idade = atual - nascimento
    print('Você nasceu em {} e tem {} anos.'.format(nascimento, idade))
    if idade == 18:
        print('Você tem {} anos e deve se alista ao exército!'.format(idade))
    elif idade < 18:
        print('Ainda faltam {} anos para se alistar.'
              '\nSeu alistamento será no ano de {}.'.format(idade - 18, nascimento + 18))
    elif idade > 18:
        print('Você deveria ter se alistado em {}.'.format(nascimento + 18))
else:
    print('Você está liberada do alistamento obrigatório!')

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunta nota:' ))
m = (n1 + n2) / 2

print('Tirando {} e {} sua média é de {}.'.format(n1, n2, m))

if m >= 7.0:
    print('PARABÉNS!!! Você está acima da média e foi APROVADO!')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO!!!')
else:
    print('REPROVADO!!!')

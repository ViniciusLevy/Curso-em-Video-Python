r1 = float(input('Digite um valor para reta: '))
r2 = float(input('Digite um valor para reta: '))
r3 = float(input('Digite um valor para reta: '))
if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('É possível formar um triângulo com estas retas!')
else:
    print('Não é possível formar um triângulo com estas retas!')

r1 = float(input('Digite um valor para reta: '))
r2 = float(input('Digite um valor para reta: '))
r3 = float(input('Digite um valor para reta: '))
if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos acima NÂO PODEM FORMAR um triângulo!')

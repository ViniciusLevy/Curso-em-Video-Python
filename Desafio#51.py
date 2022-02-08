p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
décimo = p1 + (10 - 1) * r
for c in range(p1, décimo + r, r):
    print(c, end=' >')
print('Acabou!')

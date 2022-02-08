nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('Este nome possui {} letras.'.format(len(nome.replace(' ', ''))))
nome1 = nome.split()
print('O primeiro nome possui {} letras.'.format(len(nome1[0])))


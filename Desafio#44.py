print(f'{"LOJAS LEVY":=^40}')
preco = float(input('Valor das compras: '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a opção de pagamento? '))
if opcao == 1:
    total = preco * 0.9
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
    parc = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f}.'.format(parc))
elif opcao == 4:
    totalparc = int(input('Quantas parcelas? '))
    total = preco * 1.2
    parc = total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(totalparc, parc))
else:
    total = preco
    print('Por favor, digite uma das opções válidas de pagamento! TENTE NOVAMENTE!')
print('Sua compra de R$ {:.2f} vai custa R$ {:.2f} no final.'.format(preco, total))

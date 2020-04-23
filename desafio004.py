def ground_shipping_cost(peso):
    if peso <= 2.00:
        preco__por_kilo = 1.50
    elif peso <= 6.00:
        preco_por_kilo = 3.00
    elif peso <= 10.00:
        preco_por_kilo = 4.00
    else:
        preco_por_kilo = 4.75
    return 20 + (preco_por_kilo * peso)

print(ground_shipping_cost(8))



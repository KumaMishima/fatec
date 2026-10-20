#10. Cálculo de Desconto (Aritmética e Decisão)
#Peça o valor de um produto (real). Se o produto custar mais de R$ 100.00, aplique um desconto de 10% e
#mostre o preço final. Senão, exiba o preço original.

preco_produto = float(input('Digite o preço do produto: '))
if preco_produto > 100.00:
    preco_final = preco_produto * 0.9
    print(f'Preço final com desconto: R$ {preco_final}')
else:
    print(f'Preço original: R$ {preco_produto}')

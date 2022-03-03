print('==' * 20)
print('          LOJA SUPER BARATÃO')
print('==' * 20)
cont = soma = maismil = menor = barato = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco >= 1000:
        maismil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('\033[1;31mFim do programa !!\033[m')
print('==' * 20)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maismil} Produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
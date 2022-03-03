t = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
     'Estojo', 25.00, 'Transferidor', 4.20,
     'Compasso', 9.99, 'Mochila', 120.32,
     'Canetas', 22.30, 'Livro', 34.90)
v = 0
print('-' * 30)
print(f'{" LISTA DE PREÇOS ":^30}')
print('-' * 30)
for c in t:
    if type(c) is str:
        print(f'{c:.<20}R$ ', end='')
    if type(c) is float:
        print(f'{c:>7.2f}')
        v += c
print(f'\033[:31m{"Total":.<20}R$ {v:>7}\033[m')
print('-' * 30)
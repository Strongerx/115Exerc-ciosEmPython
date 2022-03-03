
def dobro(n):
    return n * 2


def aumentar(n):
     return n + (n * 20 / 100)


def diminuir(n):
    return  n - (n * 12/100)


def metade(n):
    return  n / 2


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


def resumo(p):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado:  \t{moeda(p)}')
    print(f'Dobro do preço:   \t{moeda(dobro(p))}')
    print(f'Metade do preço:  \t{moeda(metade(p))}')
    print(f'20% de aumento:   \t{moeda(aumentar(p))}')
    print(f'12% de redução    \t{moeda(diminuir(p))}')
    print('=' * 30)



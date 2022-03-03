def dobro(n):
    return n * 2


def aumentar(n):
     return n + (n * 10 / 100)


def diminuir(n):
    return  n - (n * 13/100)


def metade(n):
    return  n / 2


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

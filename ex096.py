print()
print('Controle de Terrenos')
print('=='*10)

def r(l, c):
    r = l * c
    print(f'A area de um terreno {l}x{c} é de {r}m')


l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
r(l, c)

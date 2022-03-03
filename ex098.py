from time import sleep

def contador(inicio, fim, passo):
    print(inicio, end=' ')
    sleep(1)
    while True:
        if fim > inicio:
            c = (inicio + passo)
            print(c, end=' ')
            sleep(1)
            inicio = c
            if c >= fim:
                break
        elif fim < inicio:
            c = (inicio - passo)
            print(c, end=' ')

            sleep(1)
            inicio = c
            if c <= fim:

                break

#principal
#a)
print('Contagem 1:')
contador(1, 10, 1)
print()
print('-'*25)
#b)
print('\nContagem 2:')
contador(10, 0, 2)
print()
print('-'*25)
resp = str(input('\nVocê deseja fazer uma contagem personalizada? [S/N] '))
while resp in 'Ss':
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o pulo da contagem: '))
    print('\nContagem personalizada:')
    contador(inicio, fim, passo)
    print()
    print('-' * 25)
    resp = str(input('\nVocê deseja fazer uma contagem personalizada? [S/N] '))
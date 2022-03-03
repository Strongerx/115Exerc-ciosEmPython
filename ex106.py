def interface():
    from time import sleep
    while True:
        print('\033[43m-=' * 20)
        print('        SISTEMA DE AJUDA PyHELP')
        print('-=' * 20)
        print('\033[m')
        r = str(input('Função ou Biblioteca > ')).lower()
        if r == 'fim':
            print('\033[1;41m-=' * 20)
            print(' Até logo')
            print('-=' * 20)
            print('\033[m')
            break
        print('\033[46m-=' * 20)
        print(f'    Acessando o manual do comando "{r}"')
        print('-=' * 20)
        print('\033[m')
        sleep(3)
        print('\033[7;40m')
        help(f'{r}')
        print('\033[m')



interface()
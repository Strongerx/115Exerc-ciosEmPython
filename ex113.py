try:
    ni = int(input('Digite um Inteiro:'))
except:
    print('\033[1;31mERRO: por favor, digite um número inteiro valido\033[m')
    ni = int(input('Digite um Inteiro:'))
try:
    nr = float(input('Digite um Real: '))
except:
    print('\033[1;31mERRO: por favor, digite um número Real valido\033[m')
    nr = int(input('Digite um Real:'))
finally:
    print(f'\033[1;32mO valor inteiro digitado foi {ni} e o real foi {nr}')

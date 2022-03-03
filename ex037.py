numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print ('{} convertido para BINARIO é igual a \33[1;31m{}\33[m'.format(numero, bin(numero)[2:]))
elif op == 2:
    print ('{} convertido para OCTAL é igual a \33[1;31m{}\33[m'.format(numero, oct(numero)[2:]))
elif op == 3:
    print ('{} convertido para HEXADECIMAL é igual a \33[1;31m{}\33[m'.format(numero, hex(numero)[2:]))
else:
    print('\33[1;31mOpção invalida tente novamente !!\33[m')
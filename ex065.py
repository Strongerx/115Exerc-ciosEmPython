cont = 0
n = 'n'
r = 0
soma = maior = menor = 0
while r != 'N':
    numero = float(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / cont

print('Você digitou {} numeros e a média foi de {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
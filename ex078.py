valor = []
maior = menor = cont = 0
for c in range(0, 5):
    valor.append(int(input(f'Digite um valor para a Posição {c}: ')))
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} nas posições ', end=' ')
for i, v in enumerate(valor):
    if v == max(valor):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valor)} nas posiçoes ', end=' ')
for i, v in enumerate(valor):
    if v == min(valor):
        print(f'{i}... ', end='')







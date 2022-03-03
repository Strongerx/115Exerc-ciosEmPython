totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = 2021 - pessoa
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('o número de pessoas menor é de {}'.format(totmenor))
print('o número de pessoas de maior é de {}'.format(totmaior))

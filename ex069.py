print('==' * 20)
print('          CADASTRE UMA PESSOA')
print('==' * 20)
cont = 0
totalm = 0
demaior = 0
mulhervinte = 0
p = 'S'
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        demaior += 1
    if sexo == 'M':
        totalm += 1
    if sexo == 'F' and idade < 20:
        mulhervinte += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if p == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {demaior}')
print(f'Ao todo temos {totalm} homens cadastrados')
print(f'E temos {mulhervinte} mulheres com menos de 20 anos')



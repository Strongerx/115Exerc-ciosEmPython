dados = {}
galera = []
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! por favor, digite somente M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print('Erro! Responda apenas s ou n')
    if r == 'N':
        break
print('-=' * 30)
print(f'Fora cadastrada {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A Média de idade das pessoas é de {media:5.2f} anos')
print(f'As mulheres cadastras foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas q estão acima da média: ', end='')
for p in galera:
    if p ['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

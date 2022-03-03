dado = {}
dado['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
idade = 2021 - ano
dado['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dado['carteira'] != 0:
    dado['contratação'] = int(input('Ano de Contratação: '))
    dado['Salario'] = float(input('Salário: '))
    dado['Aposenta'] = idade + (dado['contratação'] + 35) - 2021
print('-=' * 30)
for k, v in dado.items():
    print(f'  -  {k} tem o valor {v}')



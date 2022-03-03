pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Media'] = float(input('Média: '))
print('-=' * 20)
print(f'- nome é igual a {pessoa["Nome"]}')
print(f'- média é igual a {pessoa["Media"]}')
if pessoa["Media"] >= 7:
    print('- situação é igual a Aprovado')
elif pessoa["Media"] < 7 and pessoa["Media"] >= 5:
    print('- situação é igual a Recuperação')
else:
    print('- situação é igual a Reprovado')
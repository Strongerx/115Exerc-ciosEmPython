def voto():
    print('-=' * 15)
    ano = int(input('Em que ano você nasceu? '))
    idade = 2021 - ano
    if idade >= 18:
        print(f'Com {idade}: Voto Obrigatorio.')
    elif idade <= 16 < 18 or idade > 65:
        print(f'Com {idade}: Voto Opcional')
    elif idade < 16:
        print(f'Com {idade}: Voto Opcional')
voto()
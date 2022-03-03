ano = int(input('\33[1;31mAno de nascimento:\33[m '))
idade = 2021 - ano
passou = 2021 - ano - 18
print ('Quem nasceu em \33[1;31m{}\33[m tem \33[4;31m{}\33[m anos em 2021. '.format(ano, idade))
if idade == 18:
    print ('Você tem que se alistar \33[1;31mIMEDIATAMENTE !!\33[m')
elif idade < 18:
    print ('Ainda faltam \33[4;31m{}\33[m anos para o alistamento'.format(18 - idade))
    print ('Seu alistamento será em \33[1;31m{}\33[m'.format(ano + 18))
elif idade > 18:
    print('Você ja deveria ter se alistado há \33[4;31m{}\33[m anos.'.format(passou))
    print('Seu alistamento foi em \33[1;31m{}\33[m'.format(ano + 18))


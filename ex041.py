ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
print ('O atleta tem \33[4;31m{}\33[m anos.'.format(idade))
if idade <= 9:
    print('Classificação: \33[1;32mMIRIM\33[m')
elif idade <= 14:
    print ('Classificação: \33[1;32mINFANTIL\33[m')
elif idade <= 19:
    print('Classificação: \33[1;32mJUNIOR\33[m')
elif idade <= 25:
    print('Classificação: \33[1;32mSENIOR\33[m')
elif idade > 25:
    print ('Classificação: \33[1;32mMASTER\33[m')
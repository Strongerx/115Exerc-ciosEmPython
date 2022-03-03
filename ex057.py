s = str(input('Informe o sexo: [M/F] ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Dados invalidos, Digite novamente: [M/F] ')).upper()[0].strip()
print('Sexo {} registrado com sucesso !!'.format(s))
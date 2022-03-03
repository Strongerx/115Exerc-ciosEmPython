n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
vl = (n1 + n2) /2
print ('Tirando {} e {}, a média do aluno é de {} !!'.format(n1, n2, vl))
if vl > 7:
    print('O aluno está \33[1;32mAPROVADO !!\33[m'.format(vl))
elif vl >=5 and vl < 7:
    print ('O aluno está de \33[1;34mRECUPERAÇãO !!\33[m'.format(vl))
elif vl < 5:
    print('O aluno está \33[1;31mREPROVADO !!\33[m'.format(vl))
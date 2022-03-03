salario = float(input('Qual é o salário do funcionario? R$'))
if salario > 1250:
    sl1 = salario * 10/100
    sl2 = salario + sl1
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora. '.format(salario, sl2))
else:
    sl1 = salario * 15/100
    sl2 = salario + sl1
    print('Quem ganhava R${} passa a ganhar R${:.2f} agora. '.format(salario, sl2))

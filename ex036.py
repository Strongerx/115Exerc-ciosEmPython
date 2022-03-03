valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor / (anos * 12)
minimo = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('\33[1;31mAcesso negado\33[m!!')

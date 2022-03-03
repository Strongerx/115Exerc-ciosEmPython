print ('{:=^40}'.format('- |Leuzin| -'))
preço = float(input('Preço das compras : \33[1;32mR$\33[m' ))
print ('\33[1;32mFORMAS DE PAGAMENTO\33[m')
print ('[ 1 ] A vista dinheiro/cheque')
print ('[ 2 ] A vista cartão')
print ('[ 3 ] 2x no cartão ')
print ('[ 4 ] 3x ou mais no cartão')
op = int(input('Qual a sua opção? '))
if op == 1:
    total = preço - (preço * 10 / 100)
elif op == 2:
    total = preço - (preço * 5 / 100)
elif op == 3:
    total = preço
    parcela = total / 2
    print ('Sua compra será parcelada em 2x de \33[1;32mR${}\33[m SEM JUROS'.format(parcela))
elif op == 4:
    total = preço + (preço * 20 / 100)
    totalpa = int(input('Quantas parcelas?? '))
    parcela = total / totalpa
    print ('Sua compra sera parcelada em {}x de \33[1;32mR${:.2f}\33[m COM JUROS'.format(totalpa, parcela))
else:
    total = preço
    print ('\33[1;31mOpção invalida de pagamento, TENTE NOVAMENTE !!\33[m')
print ('Sua compra de \33[1;32mR${}\33[m vai custar \33[1;32mR${:.2f}\33[m no final.'.format(preço, total))

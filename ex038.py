n1 = float(input('\33[4;32mPrimeiro valor:\33[m'))
n2 = float(input('\33[4;32mSegundo valor:\33[m'))
if n1 > n2:
    print('\33[1;31mO primero valor é MAIOR !!\33[m')
elif n2 > n1:
    print('\33[1;31mO segundo valor é MAIOR !!\33[m')
elif n1 == n2:
    print('\33[1;31mOs valores são IGUAIS!!\33[m')
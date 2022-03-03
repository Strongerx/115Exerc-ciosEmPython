
while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('=' * 40)
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t * c}')
    print('=' * 40)
print('Programa de tabuada encerrado. Volte sempre !!')








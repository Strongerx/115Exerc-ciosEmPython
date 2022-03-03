v = float(input('Qual é a velocidade atual do do carro? '))
vl = (v-80) * 7

if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h\n'
          'Você deve pagar uma multa de R${}!'.format(vl))
else:
    print('Tenha um bom dia! Dirija com segurança! ')
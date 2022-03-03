peso = float(input('Qual é o seu peso? \33[1;34m(KG)\33[m'))
altura = float(input('Qual é a sua altura? \33[1;34m(M)\33[m'))
imc = peso / (altura ** 2)
print ('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print ('Você está \33[1;34mABAIXO DO PESO !!\33[m')
elif imc <= 25:
    print ('Você está no \33[1;32mPESO IDEAL !!\33[m')
elif imc <=30:
    print ('Você está com \33[1;31mSOBRE PESO !!\33[m')
elif imc > 30:
    print ('Você está em \33[1;31mOBESIDADE MORBIDA\33[m, cuidado !!')


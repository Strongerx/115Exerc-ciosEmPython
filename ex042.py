s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Tercerio segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 +s2:
    print('Os segmentos acima PODEM FORMAR um triangulo ',end='')
    if s1 == s2 == s3:
        print ('\33[1;31mEQUILATERO !!\33[m')
    elif s1 != s2 != s3 != s1:
        print ('\33[1;31mESCALENO !!\33[m')
    else:
        print ('\33[1;31mISOSCELES !!\33[m')
else:
    print ('Os segmentos acima \33[1;31mNAO PODEM FORMAR\33[m um triangulo')
f = str(input('Digite uma frase para saber se é um palindroma: ')).strip().upper()
palavras = f.strip()
junto = ''.join(palavras)
inverso = junto[::-1]
print('Você digitou a frase {}'.format(f))
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('é um palindromo !!')
else:
    print('não é um palindromo !!')
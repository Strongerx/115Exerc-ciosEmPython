def notas(*n, sit=False):
    '''
    ->Função para analisar notas e situações de varios alunos
    :param n: uma ou mais notas de alunos
    :param sit: situação
    :return: retorna o valor
    '''
    r = {}
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] > 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
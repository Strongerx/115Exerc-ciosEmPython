from ex115A import *
from time import sleep
from ex115A.arquivo import *

arq = 'cusoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)



menu(['opç=1, opç=2, opç=3'])
while True:
    r = int(input('Sua opção: '))
    if r == 1:
        cabe('Opção 1')
    elif r == 2:
        cabe('Opção 2')
    elif r == 3:
        cabe('Saindo do sistema... Até logo')
        break
    else:
        cabe('Erro ! Digite uma opção valida')
    sleep(2)
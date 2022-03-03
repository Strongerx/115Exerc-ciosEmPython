def linha(tam= 42):
    return '=' * tam



def cabe(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabe('MENU PRINCIPAL')

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistma ')
    print(linha())

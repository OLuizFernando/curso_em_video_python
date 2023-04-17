def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[31mHouve um erro na criação do arquivo \'{nome}\'.\033[m')
    else:
        print(f'\033[32mArquivo \'{nome}\' criado com sucesso.\033[m')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo.')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<32}{dado[1]:>3} ano(s)')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'\033[31mHouve um erro na abertura do arquivo \'{arq}\'.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro ao escrever os dados.')
        else:
            print(f'\033[32mRegistro de {nome} adicionado.\033[m')
            a.close()
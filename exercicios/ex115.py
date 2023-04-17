from modulos.ex115.lib.interface import *
from modulos.ex115.lib.arquivo import *
from modulos.uteis.cores import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    resposta = menu(['Ver Cadastros', 'Novo Cadastro', 'Sair'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().title().replace(' De ', ' de ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('SAINDO...')
        break
    else:
        print(vermelho('ERRO: Digite uma opção válida.'))
    sleep(1)
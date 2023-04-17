from modulos.uteis.cores import *
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(vermelho("Site 'pudim.com.br' indisponível."))
else:
    print(verde("Site 'pudim.com.br' acessível."))
# com essas importaçõs de bibliotecas eu consigo verificar se é possivel acessa um código ou não
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento')
else:
    print('Consegui acessar o site pudim com sucesso !')
    #para obter o código do site inteiro
    print(site.read())

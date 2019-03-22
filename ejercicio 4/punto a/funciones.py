from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def item_equipos():
    lista1=['1. Deportivo Cali','2. America de Cali','3. Atletico Nacional','4. Independiente Medellin ','5. Todos', '0. Salir']
    cadena=json.dumps(lista1)
    return cadena

def item_continuar():
    lista=['1. Continuar','2. Salir']
    cadena=json.dumps(lista)
    return cadena

def muestra_menu(cadena):
    lista2=json.loads(cadena)
    for i in lista2:
        print( i)

def datos_equi(url):
	try:
		html=urlopen(url)
	except:
		print('url no funciona')
		pass
	try:
		bsObj=BeautifulSoup(html.read(), 'html.parser')
		nombre_equi=bsObj.find('h1', {'id':'firstHeading'}).get_text()
		div_cont=bsObj.find_all('p')
		historia_equi=[]
		for c in div_cont:
			historia_equi.append(c.get_text())
		print(str(nombre_equi)+'\n'+str(historia_equi)+'\n')
	except AttributeError as e:
		print('url no funiona')
	

import json

TAM_MAX_CLAVE = 26 #tamaño del alfabeto, valor constante

def menuentrada(): #lista las opciones que habra en el mene, para luego recorrerlas e imprimirlas con la funcion menu lista
	lista=['1. Encriptar mensaje', '2. Desencriptar mensaje', '3. Salir']
	cadena=json.dumps(lista)
	return cadena

def menu_lista(cadena): #imprime una lista en pantalla
	lista=json.loads(cadena)
	for i in lista:
		print( i)

def obtener_clave(): #pide y verifica que la clave este entre el rango 1-26
	clave = 0
	while True:
		print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
		clave = int(input())
		if (clave >= 1 and clave <= TAM_MAX_CLAVE):
			return clave

def obtenerMensajeTraducido(modo, mensaje, clave): #funcion para encriptar o desincreptar el mensaje
	if modo == "2":
		clave= -clave
	traduccion = ''
	
	for simbolo in mensaje:
		if simbolo.isalpha():
			num = ord(simbolo)
			num += clave

			if simbolo.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif simbolo.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			traduccion += chr(num)
		else:
			traduccion += simbolo
	return traduccion
import json

def item_sentencias():
    lista1=['\n¿Qué desea realizar en la base de datos?','1. Consultar Información','2. Insertar Datos','3. Actualizar Datos','4. Eliminar un resgistro','5. Salir']
    cadena=json.dumps(lista1)
    return cadena

def item_consultas():
    lista1=['\n¿Qué información desea ver?','	1. Toda las tablas','	2. Registros de una tabla','	3. Atrás']
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


from socket import socket
import funcion #archivo con funciones necesarias
import json


def main():
    s = socket()
    s.connect(("localhost", 6030))
    siga = True #variable bandera, indica si continuar o salir de conexión
    while siga:
        peticion=[]
        menu=funcion.menuentrada()
        listamenu=funcion.menu_lista(menu)
        queHacer = input("> ")
        peticion.append(queHacer)
        if int(queHacer) == 1:#el usuario desea encripat mensaje
            men_=input("ingrese su mensaje >>")
            peticion.append(men_)
            clave = funcion.obtener_clave()
            peticion.append(clave)
        elif int(queHacer) == 2:#el usuario desea desencripat mensaje
            men_=input("ingrese su mensaje >>")
            peticion.append(men_)
            clave = funcion.obtener_clave()
            peticion.append(clave)
        else:#el usuario desea salir
            print("hasta luego")
            s.close()
            siga=False

        try:
            cadena_envio=json.dumps(peticion)
            s.send(str(cadena_envio).encode())
            datos = s.recv(1024)
            if datos:
                print("Su mensaje traducido es: ")
                print(datos.decode())
        except:
            pass


if __name__ == "__main__":
    main()
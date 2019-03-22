import socket, time
import funciones
import json
import bd


def main():
    ruta_s= socket.socket()
    #coneccion con el servidor
    ruta_s.connect(("localhost",33300))
    datos_oper = []

    sigue=True
    try:
        while sigue:
            datos_conBD=[]
            if sigue:
                print('Bienvenido\nEste programa permite realizar una conexión a una base de datos según unos datos dados\n')
                datos_conBD.append(input("Ingrese el Host (por defecto '127.0.0.1')"))
                if "" == datos_conBD[0]:
                    datos_conBD[0]="127.0.0.1"
                datos_conBD.append(input("Ingrese el Usuario (por defecto 'root')"))
                if datos_conBD[1]=="":
                    datos_conBD[1]="root"
                datos_conBD.append(input("Ingrese la Contraseña (por defecto '')"))
                datos_conBD.append(input("Ingrese el nombre de la Base de Datos (por defecto 'ej4puntod')"))
                if "" == datos_conBD[3]:
                    datos_conBD[3]="ej4puntod"

                conn_bd = bd.BaseDatos(datos_conBD)#se conecta a la Bd indicada por el usuario
                
                while conn_bd.bandera: #variable donde True == estar conectado a la Bd, False == desconectado bd

                    funciones.muestra_menu(funciones.item_sentencias())
                    opt = input("Seleccione una opción >> ")
                    if int(opt)==1:
                        sigue2=True
                        while sigue2:
                            funciones.muestra_menu(funciones.item_consultas())
                            opt2 = input("Seleccione una opción >> ")
                            if int(opt2) == 1:
                                conn_bd.consultar_tablas()
                            elif int(opt2) == 2:
                                tabla = input("Ingrese el nombre de la tabla >> ")
                                query = "SELECT * FROM "+tabla
                                conn_bd.consultar_registros(query)
                            elif int(opt2) == 3:
                                sigue2 = False
                            else:
                                print("Opción equivocada, hasta luego...")
                                sigue2 = False
                            
                    elif int(opt)==2:
                        datos_us = []
                        print("\nSe va a insertar un registro en la tabla 'tabla_prueba'")
                        datos_us.append(input("Ingrese un nombre >> "))
                        datos_us.append(input("Ingrese un apellido >> "))
                        datos_us.append(input("Ingrese un correo >> "))
                        numero = input("Ingrese un numero celular >> ")
                        bandera_num=True
                        while bandera_num:
                            if len(numero) == 10:
                                bandera_num=False
                                datos_us.append(numero)
                            else:
                                numero=input("\nIngrese un numero correcto celular >> ")
                        datos_us.append(numero)

                        conn_bd.insertar_regi(datos_us)
                        conn_bd.consultar_registros("SELECT * FROM tabla_prueba")

                        
                    elif int(opt)==3:
                        conn_bd.consultar_registros("SELECT * FROM tabla_prueba")
                        id_tabla = input("\nIndique el 'id_tabla' del registro que desea Modificar >> ")
                        conn_bd.actualizar_registro(id_tabla)

                    elif int(opt)==4:
                        conn_bd.consultar_registros("SELECT * FROM tabla_prueba")
                        id_tabla = input("\nIndique el 'id_tabla' del registro que desea Eliminar>> ")
                        conn_bd.eliminar_registro(id_tabla)
                    elif int(opt)==5:
                        conn_bd.cerrar_conn()
                        sigue = False
                    else:
                        datos_oper.append('cerrar')
                        cadena_envio = json.dumps(datos_oper)
                        ruta_s.send(cadena_envio.encode())
                        sigue=False
                        break

        #envia al servidor la indicación de cerrar
        datos_oper.append('cerrar')
        cadena_envio = json.dumps(datos_oper)
        ruta_s.send(cadena_envio.encode())
        
        #imprime en pantalla respuesta del servidor
        datos = ruta_s.recv(1024)
        resp=json.loads(datos.decode())
        print (resp)
        ruta_s.close()
    except:
            print('\nHasta luego...')
            ruta_s.close()


if __name__ == '__main__':
    main()
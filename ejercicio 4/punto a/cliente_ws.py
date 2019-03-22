import socket
import funciones
import json, time


def main():
    ruta_s= socket.socket()
    #coneccion con el servidor
    ruta_s.connect(("localhost",33000))

    #direcciones web para hacer scraping
    url_cali="https://es.wikipedia.org/wiki/Deportivo_Cali"
    url_america="https://es.wikipedia.org/wiki/Am%C3%A9rica_de_Cali"
    url_nacional="https://es.wikipedia.org/wiki/Atl%C3%A9tico_Nacional"
    url_medellin="https://es.wikipedia.org/wiki/Independiente_Medell%C3%ADn"

    sigue=True
    try:
        while sigue:
            datos_oper = []
            if sigue:
                print('Bienvenido\nEste es un web scraping que rescata información de algunos equipos de futbol colombiano')
                funciones.muestra_menu(funciones.item_equipos())
                opt= input("Seleccione una opción >> ")
                datos_oper.append(opt)
                if int(opt)==1:
                    funciones.datos_equi(url_cali)
                elif int(opt)==2:
                    funciones.datos_equi(url_america)
                elif int(opt)==3:
                    funciones.datos_equi(url_nacional)
                elif int(opt)==4:
                    funciones.datos_equi(url_medellin)
                elif int(opt)==5:
                    funciones.datos_equi(url_cali)
                    funciones.datos_equi(url_america)
                    funciones.datos_equi(url_nacional)
                    funciones.datos_equi(url_medellin)
                else:
                    datos_oper.append('cerrar')
                    cadena_envio = json.dumps(datos_oper)
                    ruta_s.send(cadena_envio.encode())
                    sigue=False
                    #imprime en pantalla respuesta del servidor
                    datos = ruta_s.recv(1024)
                    resp=json.loads(datos.decode())
                    print (resp)
                    break

            funciones.muestra_menu(funciones.item_continuar())
            opc=input('seleciones una opción >> ')

            if int(opc)!=1:
                datos_oper.append('cerrar')
                cadena_envio = json.dumps(datos_oper)
                ruta_s.send(cadena_envio.encode())
                sigue=False
                break
        
        
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
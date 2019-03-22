from socket import socket,error
from threading import Thread
import funciones



class Cliente(Thread):
    def __init__(self,conexion,direccion):
        Thread.__init__(self)
        self.conexion=conexion
        self.direccion=direccion

    def run(self):
        while True:
            try:
                mensaje_c=self.conexion.recv(1024)
                mens_cliente = json.loads(mensaje_c.decode())
            except error:
                print ("[%s] Error de lectura" %self.name)
                break
            else:
                if mens_cliente[1] == 'cerrar':
                    try:
                        respuest="Hasta luego"
                        self.conexion.send(respuest.encode())
                    except:
                        pass

def main():
    server=socket()
    server.bind(("localhost", 33000))
    server.listen(1)
    while True:
        con,dire=server.accept()
        print(dire[0]+ " conectado")
        hilo = Cliente(con,dire)
        hilo.start()

if __name__ == '__main__':
    main()
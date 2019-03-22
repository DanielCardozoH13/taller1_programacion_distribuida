from socket import socket,error
from threading import Thread


pelicula = list()
ventas = list()
class Cliente(Thread):
    def __init__(self,conexion,direccion):
        Thread.__init__(self)
        self.conexion=conexion
        self.direccion=direccion

    def run(self):
        while True:
            try:
                mensaje_c=self.conexion.recv(1024)
            except error:
                print ("[%s] Error de lectura" %self.name)
                break
            else:
                if mensaje_c != 'salir':
                    if mensaje_c:
                        self.conexion.send("Gracias por jugar!".encode())

def main():
    server=socket()
    server.bind(("localhost", 34500))
    server.listen(1)
    while True:
        con,dire=server.accept()
        print(dire[0]+" se ha unido al juego")
        hilo = Cliente(con,dire)
        hilo.start()

if __name__ == '__main__':
    main()
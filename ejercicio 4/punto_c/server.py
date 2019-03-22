from socket import socket, error
from threading import Thread
import funcion, json


class Client(Thread):
    def __init__(self, socket_cliente, datos_cliente):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos = datos_cliente


    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                mensaje_cli = self.socket.recv(1024)
                if mensaje_cli:
                    peticion_cl=json.loads(mensaje_cli)
                    respuesta_cl=funcion.obtenerMensajeTraducido(peticion_cl[0],peticion_cl[1],peticion_cl[2])
                

            except: 
                print("[%s] Error de lectura o cliente desconectado." ) #imprime en pantalla si hubo error
                break
            else:
                # .
                try:
                    if peticion_cl[0] !=3:
                        if respuesta_cl:
                            self.socket.send(respuesta_cl.encode())
                    else:
                        print("Hasta luego")
                        break
                except:
                    pass


def main():
    s = socket()
    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print("Conectado " + addr[0])
        hilo = Client(conn, addr)  # se crea hilo para atender al cliente
        hilo.start()


if __name__ == "__main__":
    main()

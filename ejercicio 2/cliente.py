import socket
import threading
import sys

class Cliente():
    def __init__(self, host="localhost", puerto=9090):
        self.sock = socket.socket()
        self.sock.connect((host, puerto))

        mensaje_servidor = threading.Thread(target=self.mensaje_server)
        mensaje_servidor.daemon = True
        mensaje_servidor.start()
        nickname= input("Bienvenido al chat 'Cebollitas', ingrese un nombre de usuario\n>> ")

        while True:
            mensaje = input()
            if mensaje != 'salir':
                mensaje=nickname+": "+mensaje
                self.enviar_mensaje(mensaje)
            else:
                self.sock.close()
                sys.exit()

    def mensaje_server(self):
        while True:
            try:
                datos = self.sock.recv(1024)
                if datos:
                    print(datos.decode())
            except:
                pass

    def enviar_mensaje(self, mensaje):
        self.sock.send(mensaje.encode())


client = Cliente()
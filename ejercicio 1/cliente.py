import socket,time
def principal():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost',9090))
    nickname=input("Bienvenido al chat \nPor favor ingrese un nombre de usuario\n>> ")

    while True:
        hora_act=time.strftime("%H:%M:%S")
        mensaje = input(nickname+">>")
        mi_socket.send(mensaje.encode())
        if(mensaje == 'salir'):
            break
        recibido=mi_socket.recv(1024)
        print(hora_act+" - server dice: "+recibido.decode())

    print("hasta luego...")
    time.sleep(2)

    mi_socket.close()


if (__name__ == '__main__'):
    principal()
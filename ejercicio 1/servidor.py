import socket, time

def principal():
    mi_socket = socket.socket()
    mi_socket.bind(("localhost",9090))
    mi_socket.listen(1)
    print('Servidor a la espera de clientes...\n')

    conexion, direccion = mi_socket.accept()
    print('Se a conectado: '+direccion[0])

    while True:
        mensaje = conexion.recv(1024)
        hora_recv = time.strftime("%H:%M:%S")
        print(hora_recv+" - "+direccion[0]+" dijó: "+mensaje.decode())
        conexion.send("Recibido".encode())
        if(mensaje.decode()== 'salir'):
            break

    print('Conexión finalizada...')
    time.sleep(2)

    conexion.close()
    mi_socket.close()

if __name__ == '__main__':
    principal()

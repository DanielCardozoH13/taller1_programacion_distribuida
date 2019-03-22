from socket import *
from threading import *
import mysql.connector
import time

clientes = {}
direcciones = {}


def configuracion():
    global servidor
    global conexion
    global cursor
    conexion = mysql.connector.connect(user="root", password="", host="localhost", database="chatmulticliente")
    cursor = conexion.cursor()
    servidor = socket()
    servidor.bind(("127.0.0.1", 9999))
    servidor.listen(10)
    print("Esperando conexiones...")
    aceptar_hilo = Thread(target=aceptar_conexiones)
    aceptar_hilo.start()
    aceptar_hilo.join()


def aceptar_conexiones():
    while True:
        cliente_local, direccion_cliente = servidor.accept()
        print("%s:%s conectado. " % direccion_cliente)
        cliente_local.send(bytes("Bienvenido, ingresa tu nombre y presiona Enter", "utf-8"))
        direcciones[cliente_local] = direccion_cliente
        Thread(target=encargarse_cliente, args=(cliente_local,)).start()


def encargarse_cliente(cliente_loc):
    nombre = cliente_loc.recv(1024).decode("utf-8")
    nombre = nombre.lower().strip()
    nuevo_cliente(nombre, cliente_loc)

    bienvenido = "Bienvenido %s! si quieres salir, escribe {salir}." % nombre
    cliente_loc.send(bytes(bienvenido, "utf-8"))

    mensaje = "%s se ha unido al chat." % nombre
    broadcast(bytes(mensaje, "utf-8"))
    clientes[cliente_loc] = nombre
    while True:
        mensaje = cliente_loc.recv(1024)
        if mensaje != bytes("{salir}", "utf-8"):
            guardar_mensaje(nombre, mensaje)
            broadcast(mensaje, nombre + ": ")
        else:
            del clientes[cliente_loc]
            broadcast(bytes("%s ha salido del chat." % nombre, "utf-8"))
            break


def broadcast(mensaje, prefix=""):
    for sock in clientes:
        sock.send(bytes(prefix, "utf-8") + mensaje)


def guardar_mensaje(nombre, mensaje):
    remitentes = clientes.values()
    for remitente in remitentes:
        sql = "INSERT INTO mensajes(texto, emisor_usuario, remitente_usuario)VALUES(%s,%s,%s)"
        parametros = (str(mensaje).strip("b"), str(nombre), str(remitente))
        cursor.execute(sql, parametros)
        conexion.commit()
        # conexion.close


def nuevo_cliente(cliente, cliente_loc):
    try:
        sql = "SELECT * FROM usuarios WHERE usuario = '%s'" % cliente
        parametros = ""
        cursor.execute(sql, parametros)
        rows = cursor.fetchall()
        if len(rows) == 0:
            try:
                sql = "INSERT INTO usuarios(usuario) VALUES ('%s')" % cliente
                cursor.execute(sql)
                conexion.commit()
            except:
                print("hubo un error")
        else:
            try:
                sql = "UPDATE usuarios SET fecha_ingreso = NULL WHERE usuario = '%s'" % cliente
                cursor.execute(sql)
                conexion.commit()
                # se envía historial al cliente
                enviar_convers(cliente, cliente_loc)
            except:
                print("hubo un error")
            # imprimir en pantalla todos los mensajes donde aparece el

    except mysql.connector.Error as err:
        print(err)


def enviar_convers(cliente, cliente_loc):
    sql = "SELECT * FROM mensajes WHERE remitente_usuario = '%s' ORDER BY fecha_enviado ASC" % cliente
    cursor.execute(sql)
    rows = cursor.fetchall()
    if len(rows) > 0:
        for row in rows:
            if row[3] == cliente:
                prefijo = ">> "
            else:
                prefijo = row[3] + ": "
            mensajes_ante = row[2].strftime("%H:%M ")+prefijo + row[1].strip("'")
            cliente_loc.send(bytes(mensajes_ante, "utf-8"))
            time.sleep(0.03)


if __name__ == "__main__":
    configuracion()

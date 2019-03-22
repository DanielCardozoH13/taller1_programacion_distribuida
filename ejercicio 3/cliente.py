from socket import *
from threading import *
from tkinter import *

def configuracion():
    interfaz()
    global cliente_socket
    cliente_socket = socket()
    cliente_socket.connect(('localhost',9999))
    
    recibir_hilo = Thread(target=recibir)
    recibir_hilo.start()
    mainloop()

def interfaz():
    global mi_mensaje, ventana, mensaje_lista
    ventana = Tk()
    ventana.title("Chat Cebollitas")
    frame = Frame(ventana)
    mi_mensaje = StringVar()
    mi_mensaje.set("")
    scroll = Scrollbar(frame)
    mensaje_lista = Listbox(frame, height=30, width=100, yscrollcommand=scroll.set,  background="#AAB7B8", font=("Arial Bold", 12))
    scroll.pack(side=RIGHT, fill=Y)
    mensaje_lista.pack(side=LEFT, fill=BOTH)
    mensaje_lista.pack()
    frame.pack()
    campo_entrada = Entry(ventana,textvariable=mi_mensaje, width=50, font=("Arial",15))
    campo_entrada.bind("<Return>",enviar)
    campo_entrada.pack()
    boton_envio = Button(ventana,text="Enviar",command=enviar, font=("Arial Bold", 10))
    boton_envio.pack()
    ventana.protocol("WM_DELETE_WINDOW", cerrando)

def recibir():
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            mensaje_lista.insert(END,mensaje)
            mensaje_lista.see(END)
        except OSError:
            break

def enviar(event=None):
    mensaje = mi_mensaje.get()
    mi_mensaje.set("")
    cliente_socket.send(bytes(mensaje, "utf-8"))
    if mensaje == '{salir}':
        cliente_socket.close()
        ventana.quit()

def cerrando(event=None):
    mi_mensaje.set("{salir}")
    cliente_socket.close()
    enviar()

if __name__ == "__main__":
    configuracion()
from socket import *
from threading import *
from tkinter import *

def configuracion():
    global cliente_socket
    cliente_socket = socket()
    cliente_socket.connect(('localhost',9999))
    interfaz()
    
    recibir_hilo = Thread(target=recibir)
    recibir_hilo.start()
    
    mainloop()

def interfaz():
    global mi_mensaje, ventana, mensaje_lista
    ventana = Tk()
    ventana.title("Triki ")
    ventana.geometry("900x500")
    ventana.resizable(width=False, height=False)
    global row_mensajes,etiqueta_titulo,row_tablero
    row_mensajes = Frame(ventana)
    mi_mensaje = StringVar()
    mi_mensaje.set("")
    
    row_mensajes.grid(row=1)

    scroll = Scrollbar(row_mensajes, orient="vertical")
    mensaje_lista = Listbox(row_mensajes, height=5, width=97, yscrollcommand=scroll.set, background="#AAB7B8", font=("Arial Bold", 12))
    mensaje_lista.grid(row=0, sticky='nw')
    scroll.grid(row=0, column=1, sticky='ns')


    campo_entrada = Entry(row_mensajes,textvariable=mi_mensaje, width=50, font=("Arial Bold",15))
    campo_entrada.bind("<Return>",enviar)
    campo_entrada.grid()
    boton_envio = Button(row_mensajes, name="boton_envio", text="Enviar", height=2, width=12, pady=5, command=enviar, font=("Arial Bold", 9))
    boton_envio.grid()


    etiqueta_titulo = Label(ventana,text="Tablero de Juego", height=3, font=("Arial Bold", 12))
    row_tablero = Frame(ventana, width=75, height=30, background="#AAB7B5")

    
    etiqueta_titulo.grid_forget( )
    row_tablero.grid_forget()

    boton11 = Button(row_tablero, name="11", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled", state="disabled")
    boton11.grid(column=1, row=2, padx=10, pady=5)

    boton12 = Button(row_tablero, name="12", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton12.grid(column=2, row=2, padx=10, pady=5)

    boton13 = Button(row_tablero, name="13", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton13.grid(column=3, row=2, padx=10, pady=5)

    boton21 = Button(row_tablero,name="21", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton21.grid(column=1, row=3, padx=10, pady=5)

    boton22 = Button(row_tablero, name="22", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton22.grid(column=2, row=3, padx=10, pady=5)

    boton23 = Button(row_tablero, name="23", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton23.grid(column=3, row=3, padx=10, pady=5)

    boton31 = Button(row_tablero,name="31", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton31.grid(column=1, row=4, padx=10, pady=5)

    boton32 = Button(row_tablero, name="32", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton32.grid(column=2, row=4, padx=10, pady=5)

    boton33 = Button(row_tablero, name="33", text="___", height=10, width=10, command=enviar, font=("Arial Bold", 5), state="disabled")
    boton33.grid(column=3, row=4, padx=10, pady=5)

    ventana.protocol("WM_DELETE_WINDOW", cerrando)


def recibir():
    while True:
        try:
            mensaje = cliente_socket.recv(1024).decode("utf-8")
            if mensaje == "[PLAY]":
                row_mensajes.grid_forget()
                etiqueta_titulo.grid( sticky="n" )
                row_tablero.grid( sticky="n")
                mensaje=""
            else:
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
    enviar()
    cliente_socket.close()


if __name__ == "__main__":
    configuracion()
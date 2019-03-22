import socket
import funciones
ruta_s= socket.socket()

def main():
    ruta_s.connect(("localhost",34500))

    print('A H O R C A D O')
    

    sigue=True
    while sigue:
        if sigue:
            listaPalabras=funciones.lista_pal()
            letrasIncorrectas = ''
            letrasCorrectas = ''
            palabraSecreta = funciones.obtenerPalabraAlAzar(listaPalabras)
            juegoTerminado = False

            while True:
                funciones.mostrarTablero(funciones.imagenes_ahorca(), letrasIncorrectas, letrasCorrectas, palabraSecreta)
                # Permite al jugador escribir una letra.
                intento = funciones.obtenerIntento(letrasIncorrectas + letrasCorrectas)
                if intento in palabraSecreta:
                    letrasCorrectas = letrasCorrectas + intento

                    # Verifica si el jugador ha ganado.
                    encontradoTodasLasLetras = True

                    for i in range(len(palabraSecreta)):
                        if palabraSecreta[i] not in letrasCorrectas:
                            encontradoTodasLasLetras = False
                            break

                    if encontradoTodasLasLetras:
                        print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                        juegoTerminado = True

                else:
                    letrasIncorrectas = letrasIncorrectas + intento
                    # Comprobar si el jugador ha agotado sus intentos y ha perdido.
                    if len(letrasIncorrectas) == len(funciones.imagenes_ahorca()) - 1:
                        funciones.mostrarTablero(funciones.imagenes_ahorca(), letrasIncorrectas, letrasCorrectas, palabraSecreta)
                        print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
                        juegoTerminado = True


                # Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
                if juegoTerminado:
                    if funciones.jugarDeNuevo():
                        letrasIncorrectas = ''
                        letrasCorrectas = ''
                        juegoTerminado = False
                        palabraSecreta = funciones.obtenerPalabraAlAzar(listaPalabras)
                    else:
                        cadena_envio="jugador termino el juego"
                        sigue=False
                        break
            ruta_s.send(cadena_envio.encode())
            pass

        datos = ruta_s.recv(1000)
        resp=json.loads(datos.decode())
        print (resp)

if __name__ == '__main__':
    main()
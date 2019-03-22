import random

def imagenes_ahorca():
  imagenes_ahor = ['''
      +---+

      |   |

          |

          |

          |

          |
   =========''', '''


     +---+

     |   |

     O   |

         |

         |

         |
   =========''', '''


     +---+

     |   |

     O   |

     |   |

         |

         |
   =========''', '''


     +---+

     |   |

     O   |

    /|   |

         |

         |
   =========''', '''


     +---+

     |   |

     O   |

    /|\  |

         |

         |
   =========''', '''


     +---+

     |   |

     O   |

    /|\  |

    /    |

         |
   =========''', '''


     +---+

     |   |

     O   |

    /|\  |

    / \  |

         |
   =========''']
  return imagenes_ahor


def lista_pal():
  palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()
  return palabras

def obtenerPalabraAlAzar(listaDePalabras):
     # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
    índiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[índiceDePalabras]



def mostrarTablero(IMGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMGENES_AHORCADO[len(letrasIncorrectas)])
    print()
    print('Letras incorrectas:', end=' ')

    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()



def obtenerIntento(letrasProbadas):
     # Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')
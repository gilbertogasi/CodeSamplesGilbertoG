# -*- coding: utf-8 -*-
import random
import re

AHORCADO = ['''
        +---+
        │   │
            │
            │
            │
            │
            =========''','''

        +---+
        │   │
        O   │
            │
            │
            │
            =========''','''

        +---+
        │   │
        O   │
        │   │
            │
            │
            =========''','''

        +---+
        │   │
        O   │
       /│   │
            │
            │
            =========''','''

        +---+
        │   │
        O   │
       /│\  │
            │
            │
            =========''','''

        +---+
        │   │
        O   │
       /│\  │
        │   │
            │
            =========''','''

        +---+
        │   │
        O   │
       /│\  │
        │   │
       /    │
            =========''','''

        +---+
        │   │
        O   │
       /│\  │
        │   │
       / \  │
            =========''','''
       ''']

def ahorcado (idx):
    return AHORCADO[idx]

def juego(adivinar):
    letra = ""
    acerto = False
    dibujo = []
    erroneo = 0
    descubierto = None

    while erroneo <= 7 or descubierto == adivinar.upper():
        cadena = input("Introduzca una letra o la palabra completa: ")

        if cadena.lower() == adivinar and len(cadena) > 1:
            acerto = True
            break
        elif cadena.lower() != adivinar and len(cadena) > 1:
            acerto = False
            if erroneo <= 7:
                dibujo = ahorcado(erroneo)
            else:
                break
            erroneo += 1
        elif adivinar.find(cadena.lower()) > -1 and len(cadena) == 1:
            indice = adivinar.find(cadena)
            letra = letra + adivinar[indice].upper()
            descubierto = re.sub("[^"+letra+"]","_",adivinar.upper()) #se utilizo expresion regular para reemplazar con _ cualquier caracter que no sea los que se han descubierto
            print(descubierto)
            if descubierto == adivinar.upper():
                acerto = True
                break
        else:
            acerto = False
            if erroneo <= 7:
                dibujo = ahorcado(erroneo)
                print(dibujo)
            else:
                break
            erroneo += 1

    return acerto

if __name__ == "__main__":
    print("JUEGO DEL AHORCADO")
    palabras = ["silla","boligrafo","cama"]
    adivinar = str(random.choice(palabras))
    resultado = juego(adivinar)

    if resultado == True:
        print("Felicidades, ha descubierto la palabra")
    else:
        print("Lo siento, fallo en descubrir la palabra: {}, intente de nuevo".format(adivinar))
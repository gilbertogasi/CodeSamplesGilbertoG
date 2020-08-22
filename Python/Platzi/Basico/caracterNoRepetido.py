# -*- coding: utf-8 -*-

def buscarCaracterNoRepetido(palabra):
    noRepetidos = ""
    encontrado = False

    for i in palabra:
        if palabra.count(i) == 1 and encontrado == False:
            noRepetidos = i
            encontrado = True

    return noRepetidos

if __name__ == "__main__":
    palabra = input("Introduzca una palabra: ")

    noRepetido = buscarCaracterNoRepetido(palabra)

    if len(noRepetido) > 0:
        print("El caracter {} es el primero en la cadena que NO se encuentra repetido".format(noRepetido))
    else:
        print("Todos los caracteres de la cadena se encuentra repetidos")

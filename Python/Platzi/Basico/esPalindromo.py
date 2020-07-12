#******Programa para validar una palabra u oracion y validar si es o no palindromo
#******Se instaló la librería unidecode con la sentencia "pip install Unidecode", a fin de utilizar la función unidecode.unidecode para transformar los caracteres de UNICODE a ASCII
# -*- coding: utf-8 -*-

import unidecode

def entramar (cadena):
    # Función para entramar un texto, a fin de poder comparar los mismos sin espacios ni caracteres especiales
    ncadena = ""
    nopermitido = " ,;¿?"
    for i in range(len(cadena) - 1):
        if not any(cadena[i].startswith(x) for x in nopermitido):
            ncadena = ncadena +  unidecode.unidecode(cadena[i].upper())

    return ncadena

def run ():
    cadena = input("Introduzca una palabra u oración: ")
    invertida = cadena[::-1]
    trama1 = entramar(cadena)
    trama2 = entramar(invertida)

    if trama1 == trama2:
        print("Es un Palindromo")
    else:
        print("NO es un Palindromo")

if __name__ == "__main__":
    run()
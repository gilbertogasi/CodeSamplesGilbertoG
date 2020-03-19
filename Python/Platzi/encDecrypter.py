# -*- coding: utf-8 -*-
#Programa para encriptar reemplazando las letras de una palabra por una completamente distinta.

ALPHA = "abcdefghijklmnopqrstuvwxyz "
KEY = "exws4jkl3mnb6ioh9qzy720fa8%"

def encrypter(text):
    newKey = ""
    indice = 0

    for i in range(len(text)):
        indice = ALPHA.index(text[i].lower())
        newKey = newKey + KEY[indice]
    
    return newKey

def decrypter(text):
    original = ""
    indice = 0

    for i in range(len(text)):
        indice = KEY.index(text[i].lower())
        original = original + ALPHA[indice]

    return original

if __name__ == "__main__":
    text = input("Digite una palabra: ")

    if not any(text.startswith(x) for x in ALPHA):
        print("Solo puede digitar letras de la a hasta la z, sin espacios ni caracteres especiales")
    else:
        resultado = encrypter(text)
        print("La palabra {} fue encriptada a {}".format(text, resultado))

        text_original = decrypter(resultado)
        print("El texto encriptado {} corresponde a la palabra {}".format(resultado, text_original))

# -*- coding: utf-8 -*-
#Programa para encriptar y desencriptar mensajes utilizando el alfabeto fonetico NATO (https://en.wikipedia.org/wiki/NATO_phonetic_alphabet).

NATO = {"A":"Alfa",
        "B":"Bravo",
        "C":"Charlie",
        "D":"Delta",
        "E":"Echo",
        "F":"Foxtrot",
        "G":"Golf",
        "H":"Hotel",
        "I":"India",
        "J":"Juliett",
        "K":"Kilo",
        "L":"Lima",
        "M":"Mike",
        "N":"November",
        "O":"Oscar",
        "P":"Papa",
        "Q":"Quebec",
        "R":"Romeo",
        "S":"Sierra",
        "T":"Tango",
        "U":"Uniform",
        "V":"Victor",
        "W":"Whiskey",
        "X":"X-Ray",
        "Y":"Yankee",
        "Z":"Zulu"}

def encrypter(text):
    newKey = ""

    for i in text:
        if i != " ":
            newKey = newKey + NATO[i.upper()] + " "
    
    return newKey

def decrypter(text):
    keyList = list(NATO.keys())
    valList = list(NATO.values())
    textList = text.split()
    textList = [tList.capitalize() for tList in textList]
    original = ""

    for i in textList:
        original = original + " " + keyList[valList.index(i)]

    return original.upper()

if __name__ == "__main__":
    text = input("Digite una palabra u oración: ")
    Deft = "E"
    opcion = input("Que desea realizar - (E)ncriptar o (D)esencriptar: ")

    try:
        if opcion == "E":
            resultado = encrypter(text)
            print("El equivalente NATO de la palabra / oración {} es {}".format(text, resultado))
        else:
            resultado = decrypter(text)
            print("El texto encriptado {} corresponde a la palabra {}".format(text, resultado))
    except KeyError:
        print("El caracter a encriptar no se encuentra en el diccionario NATO")
    except ValueError:
        print("El caracter a desencriptar no se encuentra en el diccionario NATO")

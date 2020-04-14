# -*- coding: utf-8 -*-
#Programa de encriptación de texto usando algoritmo de cifrado XOR

KEY = 'x'

def encrypter(text):
    newKey = ''

    for i in text:
        newKey = newKey + ' ' + bin(ord(i) ^ ord(KEY))
    
    return newKey

def decrypter(text):
    textDecrypt = ''
    l = []
    binary = ''
    decimal = 0

    l = text.split()

    for i in range(len(l)):
        binary = bin(int(l[i],2) ^ ord(KEY))
        decimal = int(binary,2)
        textDecrypt = textDecrypt + chr(decimal)

    return textDecrypt

if __name__ == '__main__':
    s = input('Digite una letra o palabra: ')

    resultado = encrypter(s)

    print('Binario resultante: {}'.format(resultado))

    resultado2 = decrypter(resultado)

    print('Cadena XOR desencriptada: {}'.format(resultado2))

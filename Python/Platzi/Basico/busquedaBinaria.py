# -*- coding: utf-8 -*-
#La busqueda binaria es un algoritmo que sirve para buscar un valor entre un grupo inmenso de valores
#basicamente se trata de partir una lista de valores a la mitad, a fin de buscar un valor de forma más
#rápida.

import math

def binary_search(numbers, nfind, low, high):
    
    if low > high:
        return False
    
    mid = math.floor((low + high) / 2)

    if numbers[mid] == nfind:
        return True
    elif numbers[mid] > nfind:
        return binary_search(numbers, nfind, low, mid - 1)
    else:
        return binary_search(numbers, nfind, mid + 1, high)

if __name__ == "__main__":
    l = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    nf = int(input("Ingresa un numero: "))

    result = binary_search (l, nf, 0, len(l) - 1)

    if result is True:
        print("El numero si esta en la lista")
    else:
        print("El número no esta en la lista")
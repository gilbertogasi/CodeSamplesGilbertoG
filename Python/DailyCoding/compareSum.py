# -*- coding: utf-8 -*-
#Daily Coding: PROGRAMA PARA VALIDAR SI UN NUMERO ES EL RESULTADO DE LA SUMA DE ALGUNO DE LOS NUMEROS DE UNA LISTA

n = [10, 15, 3, 7]
k = int(input("Introduzca un número: "))
result = False

for i in range(len(n)):
    for j in range(i + 1):
        if n[i] + n[j] == k:
          result = True
          break

print(result)
# -*- coding: utf-8 -*-

####
## Author: Gilberto A. Guerrero Caballero.
## Creation Date: 25-04-2020.
## Comentary: Programa de calificación de satisfacción del clienteS.
####

import sys
import Medidor as Med

def muestraImagen():
    califica = Med.Calificacion(estado = 0)

    VALOR = 1
    while True:
        try:
            n = int(input("""
                      Por favor indique su nivel de satisfacción con el servicio
                             [1] Totalmente Insatisfecho
                             [2] Insatisfecho
                             [3] Neutral
                             [4] Satisfecho
                             [5] Totalmente Satisfecho: """))

            n -= VALOR

            if n == 0:
                imagen = califica.total_insatisfecho()
                break
            elif n == 1:
                imagen = califica.insatisfecho()
                break
            elif n == 2:
                imagen = califica.neutral()
                break
            elif n == 3:
                imagen = califica.satisfecho()
                break
            elif n == 4:
                imagen = califica.total_satisfecho()
                break
            else:
                print('Por favor, elija una opción valida')
        except:
            print('')
            print("Error Desconocido: {}".format(sys.exc_info()[0]))
            print('')

    return imagen

if __name__ == '__main__':
    print('')
    print('NIVEL DE SATISFACCION DEL CLIENTE')

    Resultado = muestraImagen()

    print(Resultado)
    print('')
    print('Muchas gracias por la atención brindada, su respuesta es muy importante para nosotros.')
    print('')

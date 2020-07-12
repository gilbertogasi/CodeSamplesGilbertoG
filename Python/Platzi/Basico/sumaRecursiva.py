# -*- coding: utf-8 -*-
import sys

total = 0

def sumRecursiva():
    try:
        global total
        totalant = 0
        numero = int(input('Digite el número a sumar: '))
        totalant = total
        total += numero
        print('El resultado de la suma de {} + {} es igual a {}'.format(totalant,numero,total))
        sumRecursiva()
    except RecursionError:
        print('Se superó el límite de recursion permitido: {}'.format(str(sys.getrecursionlimit())))
    except ValueError:
        pass
    except KeyboardInterrupt:
        print('Proceso cancelado por medio del teclado')
    except: 
        print('Error: {}'.format(sys.exc_info()))


if __name__ == '__main__':
    sumRecursiva()

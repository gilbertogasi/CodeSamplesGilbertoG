import random


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n) Complejidad lineal (crecimiento proporcional a input)
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    print(lista)
    resultado = busqueda_lineal(lista, objetivo)
    print(f'El elemento {objetivo} {"esta" if resultado else "no esta"} en la lista')


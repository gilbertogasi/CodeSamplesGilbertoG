# -*- coding: utf-8 -*-
#Programa para crear una lista de contactos, que guarda el nombre y telefono/celular del contacto

def run():
    contact = []
    a = []

    try:
        while True:
            opcion = input("""Indique que desea hacer:
                [C]rear Agenda
                [A]gregar Nuevo Contacto
                [B]orrar Contacto
                [L]istar Contactos:
                [S]alir: """).upper()

            if opcion == "C":
                if len(contact) == 0:
                    print("Creacion de Agenda")
                    nombre = input("Nombre Completo del Contacto: ")
                    telefono = input("Numero de Telefono/Celular: ")
                    email = input("Correo Electrónico: ")
                    contact = [[nombre,telefono,email]]
                else:
                    print("Ya se creo una agenda, debe elegir la opcion [A]gregar Nuevo Contacto")
            elif opcion == "A":
                print("Agregar Nuevo Contacto")
                nombre = input("Nombre Completo del Contacto: ")
                telefono = input("Numero de Telefono/Celular: ")
                email = input("Correo Electrónico: ")
                a = [[nombre,telefono,email]]
                contact.extend(a)
                a = []
            elif opcion == "B":
                try:
                    elimina = int(input("Indique el numero del registro que desea borrar: "))
                    contact.pop(elimina)
                    print("")
                    print("CONTACTO BORRADO")
                    print("")
                except IndexError:
                    print("Debe elegir un numero de registro valido de 0 a n")
                except:
                    print("Error desconocido, Intente de nuevo")
            elif opcion == "L":
                print("")
                print("/******************/")
                print("Lista de Contactos: ")
                print(contact)
                print("/******************/")
                print("")
            elif opcion == "S":
                break
            else:
                print("Opción invalida, debe digitar una de las opciones listadas")
    finally:
        if len(contact) > 0:
            print("")
            print("/******************/")
            print("Lista de Contactos: ")
            print(contact)
            print("/******************/")
            print("")
            print("AGENDA GENERADA")
            print("")

if __name__ == "__main__":
    run()

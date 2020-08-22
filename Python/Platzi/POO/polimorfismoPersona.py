
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona): #clase ciclista extiende a persona

    def __init__(self, nombre):
        super().__init__(nombre) #Define la superclase


    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('Gilberto')
    persona.avanza()

    ciclista = Ciclista('Gilberto')
    ciclista.avanza()


if __name__ == '__main__':
    main()


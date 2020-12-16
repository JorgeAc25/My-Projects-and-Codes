'''

Crear una clase Coche, a través de la cual se pueda conocer el color del coche, la marca, el modelo, el número de
caballos, el número de puertas y la matricula.
Crear el constructor del coche, así como los métodos que considere necesarios.
Crear una clase PruebaCoche que instancie varios coches.

---Extra---
Permitir al usuario cambiar el color del último coche ingresado.

'''
marca = input("Ingresa la marca del vehiculo: ")
modelo = input("Ingresa el modelo del vehiculo: ")
hp = int(input("Ingresa los caballos de fuerza del vehiculo: "))
puertas = int(input("Ingresa el numero de puertas del vehiculo: "))
matricula = input("Ingresa la matricula del vehiculo: ")
color = input("Ingresa el color del vehiculo: ")


class Coche:

    # Constructor
    def __init__(self, marca, modelo, hp, puertas, matricula, color):
        self.marca = marca
        self.modelo = modelo
        self.hp = hp
        self.puertas = puertas
        self.matricula = matricula
        self.color = color

    def __str__(self):
        return "Vehículo {}, modelo {}, {} de caballos de fuerza, {} puertas, con una matricula" \
               " de {} y de color {}.".format(self.marca, self.modelo, self.hp,
                                              self.puertas, self.matricula, self.color)


class PruebaCoche:

    # Constructor
    def __init__(self, vehiculos=[]):
        self.vehiculos = vehiculos

    def cambio_color(self, vehiculos):
        self.vehiculos.pop(0)

    def agregar(self, vehiculos):
        self.vehiculos.append(vehiculos)

    def mostrar(self):
        for i in self.vehiculos:
            print(i)


vehiculo = Coche(marca, modelo, hp, puertas, matricula, color)
n = PruebaCoche([vehiculo])

while True:
    pregunta = input("Deseas agregar otro vehiculo? Y/N: ")
    if pregunta == "Y":
        marca1 = input("Ingresa la marca del vehiculo: ")
        modelo1 = input("Ingresa el modelo del vehiculo: ")
        hp1 = int(input("Ingresa los caballos de fuerza del vehiculo: "))
        puertas1 = int(input("Ingresa el numero de puertas del vehiculo: "))
        matricula1 = input("Ingresa la matricula del vehiculo: ")
        color1 = input("Ingresa el color del vehiculo: ")

        print("---Agregando vehiculo a lista---")
        n.agregar(Coche(marca1, modelo1, hp1, puertas1, matricula1, color1))

    elif pregunta == "N":
        print("---Mostrando vehiculos agregados---")
        n.mostrar()
        cambio = input("Quieres modificar el color del ultimo vehiculo? Y/N ")
        if cambio == "Y":
            n.cambio_color(Coche(marca, modelo, hp, puertas, matricula, color))
            color2 = input("Ingresa el color a cambiar: ")
            print("---Cambiando el color---")
            n.agregar(Coche(marca, modelo, hp, puertas, matricula, color2))
            n.mostrar()

        elif cambio == "N":
            print("---Fin del programa---")
            break

        else:
            print("Letra invalida, intentalo de nuevo.")
    else:
        print("Letra invalida, intentalo de nuevo.")

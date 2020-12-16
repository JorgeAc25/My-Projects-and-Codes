class Persona:
    def __init__(self, n, e):
        self.__nombre = n  # __ especifica que la variable es privada
        self.__edad = e

    # __nombre es una variable privada, por lo cual necesitaremos acceder a ella con el metodo get y set
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad


persona1 = Persona("Jorge", 20)
persona2 = Persona("Alfonso", 21)

persona2.set_nombre(input("Ingresa el nombre: "))
persona2.set_edad(22)

print("Nombre:", persona1.get_nombre(),
      "\nEdad:", persona1.get_edad())

print("Nombre:", persona2.get_nombre(),
      "\nEdad:", persona2.get_edad())

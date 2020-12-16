ancho = int(input("Ingrese el ancho del rectangulo: "))
largo = int(input("Ingrese el largo del rectangulo: "))
area = ancho * largo
perimetro = 2 * (ancho + largo)


class Rectangulo:

    # Constructor
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

    def __str__(self):
        return "Rectangulo con un perimetro de {}cm, y un area de {}cm^2".format(self.perimetro, self.area)


class PruebaRectangulo:
    rectangulos = []

    def __init__(self, rectangulos):
        self.rectangulos = rectangulos

    def agregar(self, rectangulos):
        self.rectangulos.append(rectangulos)

    def mostrar(self):
        for i in self.rectangulos:
            print(i)


rectangulo = Rectangulo(area, perimetro)
p = PruebaRectangulo([rectangulo])

while True:
    pregunta = input("Deseas agregar otro rectangulo? Y/N: ")
    if pregunta == "Y":
        ancho1 = int(input("Ingrese el ancho del rectangulo: "))
        largo2 = int(input("Ingrese el largo del rectangulo: "))

        print("---Agregando rectangulo a lista---")
        p.agregar(Rectangulo(ancho1, largo2))

    elif pregunta == "N":
        print("---Mostrando rectangulos agregados---")
        p.mostrar()
        print("---Fin del programa---")
        break
    else:
        print("Letra invalida, intentalo de nuevo.")

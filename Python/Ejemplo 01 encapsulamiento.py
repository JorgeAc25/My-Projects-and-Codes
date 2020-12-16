class Pelicula:

    #Constructor de la clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo #Creacion de atributos desde el metodo
        self.duracion=duracion
        self.lanzamiento=lanzamiento

        print("Se creo la pelicula:",self.titulo)

    def __str__(self):
        return("{} fue lanzado en {} con una duracion de {}".format(self.titulo,self.lanzamiento,self.duracion))

class Catalogo:
    peliculas=[] #Lista vacia

    #Constructor
    def __init__ (self,peliculas=[]): #Recibe como parametro la lista
        self.peliculas=peliculas

    def agregar_p(self,p):
        self.peliculas.append(p) #Agregar pelicula a la lista


    def mostrar(self): #Mostrar cantidad de peliculas en lista
        for p in self.peliculas:
            print(p)

p=Pelicula("El Padrino",180,1972)
c=Catalogo([p])
c.mostrar()

c.agregar_p(Pelicula("El Padrino: Parte 2",202,1976))
c.mostrar()
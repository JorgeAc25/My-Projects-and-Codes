from dominio.pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None

while opcion != 4:
    print("Opciones:")
    print("1. Agregar pelicula \n2. Listar peliculas \n3. Eliminar catalogo \n4. Salir")
    opcion = int(input("Escribe tu opcion (1-4) \n"))
    
    if opcion == 1:
        nombre = input("Proporciona el nombre de la pelicula: ")
        pelicula = Pelicula(nombre)
        CatalogoPeliculas.agregar(pelicula)

    elif opcion == 2:
        CatalogoPeliculas.listar()

    elif opcion == 3:
        CatalogoPeliculas.eliminar()
else:
    print("---Programa finalizado---")
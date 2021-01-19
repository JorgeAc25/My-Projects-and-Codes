import os

class CatalogoPeliculas:
    
    ruta = "peliculas.txt"

    @staticmethod
    def agregar(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta, "a") # a - modo append
            archivo.write(pelicula.__str__() + "\n")

        except Exception as e:
            print("Ha ocurrido un error al agregar " , e)

        finally:
            archivo.close()

    @staticmethod
    def listar():
        try:
            archivo = open(CatalogoPeliculas.ruta, "r")
            print("---Catalogo de peliculas---\n" + archivo.read())
        
        except Exception as e:
            print("Ocurrio un error al listar la pelicula ", e)

        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta)
            print("Archivo eliminado")

        except Exception as e:
            print("Ha ocurrido un error al eliminar el archivo ", e)
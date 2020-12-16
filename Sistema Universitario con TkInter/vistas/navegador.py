from vistas.frame_alumnos import *

from vistas.frame_profesor import *
from vistas.frame_materias import *
from vistas.frame_carreras import *
from vistas.frame_inicio import *


class App(ttk.Frame):

    def __init__(self, ventana):
        super().__init__(ventana)

        self.miVentana = ventana
        self.miVentana.title("Sistema Universitario")
        self.miVentana.geometry("1050x500")
        self.miVentana.resizable(False, False)

        # Contenedor
        self.navegador = ttk.Notebook(self)

        self.inicio = Inicio(self.miVentana)
        self.navegador.add(self.inicio,text="Inicio")

        self.alumnos = Alumnos(self.miVentana)
        self.navegador.add(self.alumnos, text="Alumnos")

        self.carreras = Carreras(self.miVentana)
        self.navegador.add(self.carreras, text="Carreras")

        self.profesor = Profesor(self.miVentana)
        self.navegador.add(self.profesor, text="Profesores")

        self.materias = Materias(self.miVentana)
        self.navegador.add(self.materias, text="Materias")

        self.navegador.pack()
        self.pack()

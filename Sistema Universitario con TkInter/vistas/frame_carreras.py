from tkinter import *
from tkinter import ttk
from conexion.consultas_db import *


class Carreras(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nueva_carrera():
            # Limpiar campos
            self.entryCarrera.delete(0, END)
            self.entryDuracion.delete(0, END)
            self.entryMatricula.delete(0, END)

            self.entryMatricula.config(state="normal")
            self.entryCarrera.config(state="normal")
            self.entryDuracion.config(state="normal")

        def agregar_datos():
            query = "INSERT INTO CARRERAS VALUES (NULL,?,?)"
            parametros = (self.entryCarrera.get(), self.entryDuracion.get())

            conexion = Conectar()
            conexion.run_db(query, parametros)
            listar_datos()

            # Limpiar campos
            nueva_carrera()

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM CARRERAS WHERE matricula_c = ?"

            conexion = Conectar()
            conexion.run_db(query, (codigo,))
            listar_datos()



        def editar_carrera():

            def actualizar(entrycarrera_nuevo, entrycarrera, entryduracion_nuevo, entryduracion):
                query = "UPDATE CARRERAS SET nombre_c = ?, duracion_c = ? WHERE nombre_c = ? AND duracion_c = ?"
                parametros = (entrycarrera_nuevo, entryduracion_nuevo, entrycarrera, entryduracion)

                conexion = Conectar()
                conexion.run_db(query, parametros)

                listar_datos()
                self.editar.destroy()

            matricula = self.tabla.item(self.tabla.selection())["text"]
            carrera_antigua = self.tabla.item(self.tabla.selection())['values'][0]
            duracion_antigua = self.tabla.item(self.tabla.selection())['values'][1]

            self.editar = Toplevel()
            self.editar.title("Editar Carrera")
            self.editar.geometry("450x200")
            self.editar.resizable(False, False)

            # Labels editar_carrera
            self.lblCarrera = Label(self.editar, text="CARRERA").place(x=100, y=20)
            self.lblMatricula = Label(self.editar, text="MATRICULA").place(x=100, y=80)
            self.lblDuracion = Label(self.editar, text='DURACION').place(x=100, y=50)

            # Entradas
            self.entryCarrera_nuevo = Entry(self.editar, width=25,
                                            textvariable=StringVar(self.editar, value=carrera_antigua))
            self.entryCarrera_nuevo.place(x=190, y=20)

            self.entryMatricula_nuevo = Entry(self.editar, width=10,
                                              textvariable=StringVar(self.editar, value=matricula), state="readonly")
            self.entryMatricula_nuevo.place(x=190, y=80)

            self.entryDuracion_nuevo = Entry(self.editar, width=15,
                                             textvariable=StringVar(self.editar, value=duracion_antigua))
            self.entryDuracion_nuevo.place(x=190, y=50)

            # Boton editar_carrera
            self.btnActualizar = Button(self.editar, text="Actualizar Carrera",
                                        command=lambda: actualizar(self.entryCarrera_nuevo.get(),
                                                                   carrera_antigua,
                                                                   self.entryDuracion_nuevo.get(),
                                                                   duracion_antigua))
            self.btnActualizar.place(x=160, y=120)


        # Labels
        self.labelReg = Label(self, text="Registrar Carrera(s)").place(x=447, y=1)
        self.labelCarrera = Label(self, text="Carrera").place(x=215, y=30)
        self.labelMatricula = Label(self, text="Matricula").place(x=215, y=60)
        self.labelDuracion = Label(self, text="Duracion").place(x=215, y=90)
        self.labelLista = Label(self, text="Lista de Carreras").place(x=450, y=175)

        # Entradas
        self.entryCarrera = Entry(self, width=25, state="readonly")
        self.entryCarrera.place(x=315, y=30)
        self.entryMatricula = Entry(self, width=15, state="readonly")
        self.entryMatricula.place(x=315, y=60)
        self.entryDuracion = Entry(self, width=15, state="readonly")
        self.entryDuracion.place(x=315, y=90)

        # Botones
        self.botonRegistro = Button(self, text='Nueva Carrera', command=nueva_carrera).place(x=525, y=40)
        self.botonGuardar = Button(self, text='Guardar Carrera', command=agregar_datos).place(x=522, y=90)
        self.botonEditar = Button(self, text="Editar Carrera", command=editar_carrera).place(x=665, y=40)
        self.botonEliminar = Button(self, text="Eliminar Carrera", command=eliminar_datos).place(x=658, y=90)

        # Tabla
        self.tabla = ttk.Treeview(self, columns=('', ''))
        self.tabla.place(x=200, y=220)
        self.tabla.heading('#0', text="MATRICULA")
        self.tabla.heading('#1', text="CARRERA")
        self.tabla.heading('#2', text="DURACION")

        # Listar datos
        def listar_datos():
            recorrer_tabla = self.tabla.get_children()

            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            query = 'SELECT * FROM CARRERAS'
            conexion = Conectar()
            datos = conexion.run_db(query)

            for carrera in datos:
                self.tabla.insert('', 0, text=carrera[0], values=(carrera[1], carrera[2]))

        listar_datos()

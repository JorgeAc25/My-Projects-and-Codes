from tkinter import *
from tkinter import ttk
from conexion.consultas_db import *


class Materias(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nueva_materia():
            self.entryMateria.delete(0, END)
            self.entryMateria.config(state="normal")
            self.comboCarrera.config(state="normal")
            self.comboProfesor.config(state="normal")

        def editar_materia():

            def actualizar(materia_n, materia_a, carrera_n, carrera_a, profesor_n, profesor_a):
                query = "UPDATE MATERIAS SET nombre_m = ?, carrera_m = ?, profesor_m = ?" \
                        " WHERE nombre_m = ? OR carrera_m = ? OR profesor_m = ?"
                parametros = (materia_n, carrera_n, profesor_n, materia_a, carrera_a, profesor_a)
                conexion = Conectar()
                conexion.run_db(query, parametros)
                listar_datos()
                self.editar.destroy()

            matricula = self.tabla.item(self.tabla.selection())['text']
            materia_antigua = self.tabla.item(self.tabla.selection())['values'][0]
            carrera_antigua = self.tabla.item(self.tabla.selection())['values'][1]
            profesor_antiguo = self.tabla.item(self.tabla.selection())['values'][2]

            self.editar = Toplevel()
            self.editar.title("Editar Materia")
            self.editar.geometry("450x250")
            self.editar.resizable(False, False)

            # Labels editar_materia
            self.lblMateria = Label(self.editar, text="MATERIA").place(x=100, y=20)
            self.lblMatricula = Label(self.editar, text="MATRICULA").place(x=100, y=50)
            self.lblCarrera = Label(self.editar, text='CARRERA').place(x=100, y=80)
            self.lblProfesor = Label(self.editar, text='PROFESOR').place(x=100, y=110)

            # Entradas
            self.entryMate = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=materia_antigua))
            self.entryMate.place(x=190, y=20)
            self.entryMatr = Entry(self.editar, width=10, textvariable=StringVar(self.editar, value=matricula))
            self.entryMatr.place(x=190, y=50)
            self.entryCar = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=carrera_antigua))
            self.entryCar.place(x=190, y=80)
            self.entryPro = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=profesor_antiguo))
            self.entryPro.place(x=190, y=110)

            # Boton editar_materia
            self.btnActualizar = Button(self.editar, text="Actualizar Materia",
                                        command=lambda: actualizar(self.entryMate.get(), materia_antigua,
                                                                   self.entryCar.get(), carrera_antigua,
                                                                   self.entryPro.get(), profesor_antiguo))
            self.btnActualizar.place(x=160, y=160)

        def agregar_materia():
            query = "INSERT INTO MATERIAS VALUES (NULL,?,?,?)"
            parametros = (self.entryMateria.get(), self.comboCarrera.get(), self.comboProfesor.get())

            conexion = Conectar()
            conexion.run_db(query, parametros)
            listar_datos()
            nueva_materia()

        def eliminar_materia():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM MATERIAS WHERE nombre_m=?"

            conexion = Conectar()
            conexion.run_db(query, (codigo,))
            listar_datos()

        # Cajas de texto
        self.comboCarrera = ttk.Combobox(self, state="disabled")
        self.comboCarrera.place(x=285, y=60)
        self.comboProfesor = ttk.Combobox(self, state="disabled")
        self.comboProfesor.place(x=285, y=90)

        def combo_carrera():
            query = "SELECT nombre_c FROM CARRERAS"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for i in datos:
                values = list(self.comboCarrera['values'])
                self.comboCarrera['values'] = values + [(i[0])]

        def combo_profesor():
            query = "SELECT nombre_p, apellidos_p FROM PROFESORES"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for i in datos:
                values = list(self.comboProfesor['values'])
                self.comboProfesor['values'] = values + [(i[0] + ' ' + i[1])]

        combo_carrera()
        combo_profesor()

        # Labels
        self.label = Label(self, text='').grid(column=1, columnspan=10, row=1, rowspan=10, padx=1000, pady=1000)
        self.labelReg = Label(self, text="Registrar Materia(s)").place(x=447, y=1)
        self.labelMateria = Label(self, text="Materia").place(x=215, y=30)
        self.labelCarrera = Label(self, text="Carrera").place(x=215, y=60)
        self.labelProfesor = Label(self, text="Profesor").place(x=215, y=90)
        self.labelMatricula = Label(self, text="Matricula").place(x=215, y=120)
        self.labelLista = Label(self, text="Lista de Materias").place(x=450, y=175)

        # Entradas
        self.entryMateria = Entry(self, width=25, state="readonly")
        self.entryMateria.place(x=285, y=30)
        self.entryMatricula = Entry(self, width=15, state='readonly')
        self.entryMatricula.place(x=285, y=120)

        # Botones
        self.botonRegistro = Button(self, text='Nueva Materia', command=nueva_materia).place(x=525, y=40)
        self.botonGuardar = Button(self, text='Guardar Materia', command=agregar_materia).place(x=522, y=90)
        self.botonEditar = Button(self, text="Editar Materia", command=editar_materia).place(x=665, y=40)
        self.botonEliminar = Button(self, text="Eliminar Materia", command=eliminar_materia).place(x=658, y=90)

        # Tabla
        self.tabla = ttk.Treeview(self, columns=('', '', ''))
        self.tabla.place(x=125, y=230)
        self.tabla.heading('#0', text="MATRICULA")
        self.tabla.heading('#1', text="MATERIA")
        self.tabla.heading('#2', text="CARRERA")
        self.tabla.heading('#3', text="PROFESOR")

        def listar_datos():
            recorrer_tabla = self.tabla.get_children()

            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            query = "SELECT * FROM MATERIAS"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for materias in datos:
                self.tabla.insert('', 0, text=materias[0], values=(materias[1], materias[2], materias[3]))

        listar_datos()

from tkinter import *
from tkinter import ttk
from conexion.consultas_db import *


class Alumnos(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo_alumno():
            self.entryNombre.delete(0, END)
            self.entryApellidos.delete(0, END)
            self.entryTelefono.delete(0, END)

            self.entryNombre.config(state="normal")
            self.entryApellidos.config(state="normal")
            self.entryTelefono.config(state="normal")
            self.comboBox.config(state="normal")

        def editar_alumno():

            def actualizar_datos(nombre_n, nombre_a, apellido_n, apellido_a, carrera_n, carrera_a, numero_n, numero_a):
                query = "UPDATE ALUMNOS SET nombre_a = ?, apellidos_a = ?, carrera_a = ?, numero_a = ?" \
                        " WHERE nombre_a = ? OR apellidos_a = ? OR carrera_a = ? OR numero_a = ?"
                parametros = (nombre_n, apellido_n, carrera_n, numero_n, nombre_a, apellido_a, carrera_a, numero_a)

                conexion = Conectar()
                conexion.run_db(query, parametros)
                listar_datos()

            matricula = self.tabla.item(self.tabla.selection())['text']
            nombre_ant = self.tabla.item(self.tabla.selection())['values'][0]
            apellidos_ant = self.tabla.item(self.tabla.selection())['values'][1]
            carrera_ant = self.tabla.item(self.tabla.selection())['values'][2]
            numero_ant = self.tabla.item(self.tabla.selection())['values'][3]

            self.editar = Toplevel()
            self.editar.title("Editar Alumno")
            self.editar.geometry("450x250")
            self.editar.resizable(False, False)

            # Labels editar_alumno
            self.lblNombre = Label(self.editar, text="NOMBRE").place(x=100, y=20)
            self.lblApellidos = Label(self.editar, text="APELLIDOS").place(x=100, y=50)
            self.lblCarrera = Label(self.editar, text='CARRERA').place(x=100, y=80)
            self.lblNumero = Label(self.editar, text='NUMERO').place(x=100, y=110)
            self.lblMatricula = Label(self.editar, text="MATRICULA").place(x=100, y=140)

            # Entradas
            self.entryNom = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=nombre_ant))
            self.entryNom.place(x=190, y=20)
            self.entryApe = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=apellidos_ant))
            self.entryApe.place(x=190, y=50)
            self.entryCar = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=carrera_ant))
            self.entryCar.place(x=190, y=80)
            self.entryNum = Entry(self.editar, width=15, textvariable=StringVar(self.editar, value=numero_ant))
            self.entryNum.place(x=190, y=110)
            self.entryMat = Entry(self.editar, width=10, textvariable=StringVar(self.editar, value=matricula),
                                  state="readonly")
            self.entryMat.place(x=190, y=140)

            # Boton editar_alumno
            self.btnActualizar = Button(self.editar, text="Actualizar Alumno",
                                        command=lambda: actualizar_datos(self.entryNom.get(), nombre_ant,
                                                                         self.entryApe.get(), apellidos_ant,
                                                                         self.entryCar.get(), carrera_ant,
                                                                         self.entryNum.get(), numero_ant))

            self.btnActualizar.place(x=160, y=180)

        def agregar_datos():
            query = "INSERT INTO ALUMNOS VALUES(NULL,?,?,?,?)"
            parametros = (
                self.entryNombre.get(), self.entryApellidos.get(), self.entryTelefono.get(), self.comboBox.get())

            conexion = Conectar()
            conexion.run_db(query, parametros)
            listar_datos()
            nuevo_alumno()

        def eliminar_datos():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM ALUMNOS WHERE matricula_a=?"

            conexion = Conectar()
            conexion.run_db(query, (codigo,))
            listar_datos()

        self.comboBox = ttk.Combobox(self, state="disabled")
        self.comboBox.place(x=315, y=120)

        def combobox():
            query = "SELECT nombre_c FROM CARRERAS"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for i in datos:
                values = list(self.comboBox['values'])
                self.comboBox['values'] = values + [(i[0])]

        combobox()

        # Labels
        self.label = Label(self, text='').grid(column=1, columnspan=10, row=1, rowspan=10, padx=1000, pady=1000)
        self.labelReg = Label(self, text="Registrar Alumno(s)").place(x=447, y=1)
        self.labelNombre = Label(self, text="Nombre(s)").place(x=225, y=30)
        self.labelApellidos = Label(self, text="Apellidos").place(x=225, y=60)
        self.labelNumero = Label(self, text="Numero de telefono").place(x=225, y=90)
        self.labelCarrera = Label(self, text="Carrera").place(x=225, y=120)
        self.labelMatricula = Label(self, text="Matricula").place(x=225, y=150)
        self.labelLista = Label(self, text="Lista de Alumnos").place(x=447, y=175)

        # Entradas
        self.entryNombre = Entry(self, width=25, state="readonly")
        self.entryNombre.place(x=315, y=30)
        self.entryApellidos = Entry(self, width=25, state="readonly")
        self.entryApellidos.place(x=315, y=60)
        self.entryTelefono = Entry(self, width=20, state="readonly")
        self.entryTelefono.place(x=355, y=90)
        self.entryMatricula = Entry(self, width=15, state="readonly")
        self.entryMatricula.place(x=315, y=150)

        # Botones
        self.botonRegistro = Button(self, text='Nuevo Alumno', command=nuevo_alumno).place(x=525, y=40)
        self.botonGuardar = Button(self, text='Guardar Alumno', command=agregar_datos).place(x=522, y=90)
        self.botonEditar = Button(self, text="Editar Alumno", command=editar_alumno).place(x=665, y=40)
        self.botonEliminar = Button(self, text="Eliminar Alumno", command=eliminar_datos).place(x=658, y=90)

        # Tabla
        self.tabla = ttk.Treeview(self, columns=('', '', '', ''))
        self.tabla.place(x=20, y=230)
        self.tabla.heading('#0', text="MATRICULA")
        self.tabla.heading('#1', text="NOMBRE")
        self.tabla.heading('#2', text="APELLIDOS")
        self.tabla.heading('#3', text="TELEFONO")
        self.tabla.heading('#4', text="CARRERA")

        def listar_datos():
            recorrer_tabla = self.tabla.get_children()

            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            query = "SELECT * FROM ALUMNOS"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for alumno in datos:
                self.tabla.insert('', 0, text=alumno[0], values=(alumno[1], alumno[2], alumno[3], alumno[4]))

        listar_datos()

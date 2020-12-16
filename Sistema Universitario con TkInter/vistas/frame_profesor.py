from tkinter import *
from tkinter import ttk
from conexion.consultas_db import *


class Profesor(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def nuevo_profesor():
            self.entryNombre.delete(0, END)
            self.entryApellidos.delete(0, END)
            self.entryTelefono.delete(0, END)
            self.comboBox.delete(0, END)
            self.entryMatricula.delete(0, END)

            self.entryNombre.config(state="normal")
            self.entryApellidos.config(state="normal")
            self.entryTelefono.config(state="normal")
            self.comboBox.config(state="normal")

        def editar_profesor():

            def actualizar(nombre_n, nombre_ant, apellido_n, apellido_ant, numero_n, numero_ant, area_n, area_ant):
                query = "UPDATE PROFESORES SET nombre_p = ?, apellidos_p = ?, numero_p = ?, area_p = ?" \
                        " WHERE nombre_p = ? OR apellidos" \
                        "_p = ? OR numero_p = ? OR area_p = ?"
                parametros = (nombre_n, apellido_n, numero_n, area_n, nombre_ant, apellido_ant, numero_ant, area_ant)

                conexion = Conectar()
                conexion.run_db(query, parametros)
                listar_datos()
                self.editar.destroy()

            matricula = self.tabla.item(self.tabla.selection())['text']
            nombre_a = self.tabla.item(self.tabla.selection())['values'][0]
            apellido_a = self.tabla.item(self.tabla.selection())['values'][1]
            numero_a = self.tabla.item(self.tabla.selection())['values'][2]
            area_a = self.tabla.item(self.tabla.selection())['values'][3]

            self.editar = Toplevel()
            self.editar.title("Editar Profesor")
            self.editar.geometry("450x250")
            self.editar.resizable(False, False)

            # Labels editar_profesor
            self.lblNombre = Label(self.editar, text="NOMBRE").place(x=100, y=20)
            self.lblApellidos = Label(self.editar, text="APELLIDOS").place(x=100, y=50)
            self.lblNumero = Label(self.editar, text='NUMERO').place(x=100, y=80)
            self.lblArea = Label(self.editar, text='AREA').place(x=100, y=110)
            self.lblMatricula = Label(self.editar, text="MATRICULA").place(x=100, y=140)

            # Entradas
            self.entryNom = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=nombre_a))
            self.entryNom.place(x=190, y=20)
            self.entryApe = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=apellido_a))
            self.entryApe.place(x=190, y=50)
            self.entryNum = Entry(self.editar, width=15, textvariable=StringVar(self.editar, value=numero_a))
            self.entryNum.place(x=190, y=80)
            self.entryAre = Entry(self.editar, width=25, textvariable=StringVar(self.editar, value=area_a))
            self.entryAre.place(x=190, y=110)
            self.entryMat = Entry(self.editar, width=10, textvariable=StringVar(self.editar, value=matricula),
                                  state="readonly")
            self.entryMat.place(x=190, y=140)

            # Boton
            self.btnActualizar = Button(self.editar, text="Actualizar Profesor",
                                        command=lambda: actualizar(self.entryNom.get(), nombre_a,
                                                                   self.entryApe.get(), apellido_a,
                                                                   self.entryNum.get(), numero_a,
                                                                   self.entryAre.get(), area_a))

            self.btnActualizar.place(x=160, y=180)

        def agergar_profesor():
            query = "INSERT INTO PROFESORES VALUES (NULL,?,?,?,?)"
            parametros = (
                self.entryNombre.get(), self.entryApellidos.get(), self.entryTelefono.get(), self.comboBox.get())

            conexion = Conectar()
            conexion.run_db(query, parametros)
            listar_datos()

        def eliminar_profesor():
            codigo = self.tabla.item(self.tabla.selection())['text']
            query = "DELETE FROM PROFESORES WHERE matricula_p=?"

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
        self.labelReg = Label(self, text="Registrar Profesor(es)").place(x=447, y=1)
        self.labelNombre = Label(self, text="Nombre(s)").place(x=215, y=30)
        self.labelApellidos = Label(self, text="Apellidos").place(x=215, y=60)
        self.labelNumero = Label(self, text="Numero de telefono").place(x=215, y=90)
        self.labelArea = Label(self, text="Area").place(x=215, y=120)
        self.labelMatricula = Label(self, text="Matricula").place(x=215, y=150)
        self.labelLista = Label(self, text="Lista de Profesores").place(x=450, y=175)

        # Entradas
        self.entryNombre = Entry(self, width=25, state="readonly")
        self.entryNombre.place(x=315, y=30)
        self.entryApellidos = Entry(self, width=25, state="readonly")
        self.entryApellidos.place(x=315, y=60)
        self.entryTelefono = Entry(self, width=20, state="readonly")
        self.entryTelefono.place(x=345, y=90)
        self.entryMatricula = Entry(self, width=15, state="readonly")
        self.entryMatricula.place(x=315, y=150)

        # Botones
        self.botonRegistro = Button(self, text='Nuevo Profesor', command=nuevo_profesor).place(x=525, y=40)
        self.botonGuardar = Button(self, text='Guardar Profesor', command=agergar_profesor).place(x=522, y=90)
        self.botonEditar = Button(self, text="Editar Profesor", command=editar_profesor).place(x=665, y=40)
        self.botonEliminar = Button(self, text="Eliminar Profesor", command=eliminar_profesor).place(x=658, y=90)

        # Tabla
        self.tabla = ttk.Treeview(self, columns=('', '', '', ''))
        self.tabla.place(x=20, y=230)
        self.tabla.heading('#0', text="MATRICULA")
        self.tabla.heading('#1', text="NOMBRE")
        self.tabla.heading('#2', text="APELLIDOS")
        self.tabla.heading('#3', text="TELEFONO")
        self.tabla.heading('#4', text="AREA")

        def listar_datos():
            recorrer_tabla = self.tabla.get_children()

            # Actualizar datos
            for elementos in recorrer_tabla:
                self.tabla.delete(elementos)

            query = "SELECT * FROM PROFESORES"
            conexion = Conectar()
            datos = conexion.run_db(query)

            for profesor in datos:
                self.tabla.insert('', 0, text=profesor[0], values=(profesor[1], profesor[2], profesor[3], profesor[4]))

        listar_datos()

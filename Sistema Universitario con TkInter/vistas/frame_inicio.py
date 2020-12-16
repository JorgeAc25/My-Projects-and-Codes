from tkinter import *
from tkinter import ttk


class Inicio(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def cerrar():
            quit()

        self.label01 = Label(self, text=" ").grid(column=1, columnspan=150, row=1, rowspan=150)
        self.cerrar = Button(self, text="Cerrar", width=10, command=cerrar).place(x=345, y=170)

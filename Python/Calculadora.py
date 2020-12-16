from tkinter import *
from math import *

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("250x520")
ventana.resizable(False, False)
ventana.configure(background="khaki")

color_botones = "floral white"
ancho_botones = 5
largo_botones = 2
operaciones = ""
memoria = ""
texto_pantalla = StringVar()


def clear():
    global operaciones
    operaciones = ""
    memoria = ""
    texto_pantalla.set("0")


def click(b):
    global operaciones
    global memoria
    operaciones += str(b)
    texto_pantalla.set(operaciones)


def resultado():
    global operaciones
    try:
        r = str(eval(operaciones))
    except:
        r = "ERROR"
    texto_pantalla.set(r)


def Save():
    global operaciones
    global memoria
    memoria = operaciones
    operaciones = ""
    memoria = str(eval(operaciones))


def Use():
    global memoria
    global operaciones
    texto_pantalla.set(operaciones or memoria)


def Delete():
    global memoria
    memoria = 0


clear()

# BOTONES
B0 = Button(ventana, text="0", command=lambda: click(0), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=0, row=5, pady=10)
BMas = Button(ventana, text="+", command=lambda: click("+"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=1, row=5, pady=10)
BC = Button(ventana, text="C", command=clear, bg="gray81", width=ancho_botones, height=largo_botones).grid(column=2,
                                                                                                           row=5,
                                                                                                           pady=10)
Bigual = Button(ventana, text="=", command=resultado, bg="gray81", width=ancho_botones, height=largo_botones).grid(
    column=3, row=5, pady=10)
B1 = Button(ventana, text="1", command=lambda: click(1), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=0, row=4, pady=10)
B2 = Button(ventana, text="2", command=lambda: click(2), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=1, row=4, pady=10)
B3 = Button(ventana, text="3", command=lambda: click(3), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=2, row=4, pady=10)
Bmenos = Button(ventana, text="-", command=lambda: click("-"), bg=color_botones, width=ancho_botones,
                height=largo_botones).grid(column=3, row=4, pady=10)
B4 = Button(ventana, text="4", command=lambda: click(4), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=0, row=3, pady=10)
B5 = Button(ventana, text="5", command=lambda: click(5), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=1, row=3, pady=10)
B6 = Button(ventana, text="6", command=lambda: click(6), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=2, row=3, pady=10)
Bmult = Button(ventana, text="*", command=lambda: click("*"), bg=color_botones, width=ancho_botones,
               height=largo_botones).grid(column=3, row=3, pady=10)
B7 = Button(ventana, text="7", command=lambda: click(7), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=0, row=2, pady=10)
B8 = Button(ventana, text="8", command=lambda: click(8), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=1, row=2, pady=10)
B9 = Button(ventana, text="9", command=lambda: click(9), bg=color_botones, width=ancho_botones,
            height=largo_botones).grid(column=2, row=2, pady=10)
Bdiv = Button(ventana, text="/", command=lambda: click("/"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=3, row=2, pady=10)
# Extra
Bsen = Button(ventana, text="sen", command=lambda: click("sin"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=1, row=6, pady=10)
Blog = Button(ventana, text="log", command=lambda: click("log"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=2, row=7, pady=10)
Braiz = Button(ventana, text="√", command=lambda: click("sqrt"), bg=color_botones, width=ancho_botones,
               height=largo_botones).grid(column=3, row=7, pady=10)
Bexp = Button(ventana, text="EXP", command=lambda: click("**"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=0, row=6, pady=10)
Bcos = Button(ventana, text="cos", command=lambda: click("cos"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=2, row=6, pady=10)
Btan = Button(ventana, text="tan", command=lambda: click("tan"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=3, row=6, pady=10)
BIzq = Button(ventana, text="(", command=lambda: click("("), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=0, row=7, pady=10)
BDer = Button(ventana, text=")", command=lambda: click(")"), bg=color_botones, width=ancho_botones,
              height=largo_botones).grid(column=1, row=7, pady=10)
# Memoria
BSav = Button(ventana, text="Save", command=Save, bg=color_botones, width=ancho_botones, height=largo_botones).grid(
    column=0, row=8, pady=10)
BUse = Button(ventana, text="Use", command=Use, bg=color_botones, width=ancho_botones, height=largo_botones).grid(
    column=1, row=8, pady=10)
BDel = Button(ventana, text="Delete", command=Delete, bg=color_botones, width=ancho_botones, height=largo_botones).grid(
    column=2, row=8, pady=10)

# Pantalla
pantalla = Entry(ventana, font=("times new roman", 14), width=20, borderwidth=15, background="azure",
                 textvariable=texto_pantalla)
pantalla.grid(column=0, columnspan=5, row=0, padx=20, pady=20)

ventana.mainloop()

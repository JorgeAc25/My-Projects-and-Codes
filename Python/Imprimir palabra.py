from tkinter import *

App = Tk()
App.title('Nombre')
App.geometry("370x200")
App.resizable(False, False)
App.configure(bg='lightblue1')


def click():
    import time
    separar = (texto.get())
    for i in separar:
        print(i)
        time.sleep(0.2)


texto = StringVar()

color_labels = "lightblue1"
color_buttons = "snow"

ventana = Frame(App)
ventana.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
ventana.rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)

# Label, caja de texto y boton
lbl1 = Label(App, text="Ingresa un texto (a-z y 0-9)",
             bg=color_labels).grid(column=2, row=1, sticky=(W, E), pady=(20, 20))

txtBox = Entry(App, width=25, bg=color_buttons, textvariable=texto).grid(
    column=2, row=3, sticky=W, pady=(10, 10))

btn1 = Button(App, text="Mostrar", bg=color_buttons,
              command=click).grid(column=2, row=4, pady=(10, 10))


App.mainloop()

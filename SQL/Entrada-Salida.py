import time
import sqlite3
from gpiozero import Button

boton = Button(17)


def presionar():
    fecha = "Fecha entrada"
    hora = time.ctime()
    print(hora)
    time.sleep(0.5)
    datos = [(fecha, hora)]
    conexion(datos)


def soltar():
    fecha = "Fecha salida"
    hora = time.ctime()
    print(hora)
    time.sleep(0.5)
    datos = [(fecha, hora)]
    conexion(datos)


def conexion(datos):
    conexion = sqlite3.connect('Fecha.db')
    c = conexion.cursor()
    c.executemany(
        "insert into acciones (verificador, fecha) values (?,?)", datos)
    conexion.commit()
    conexion.close()


boton.when_pressed = (presionar)
boton.when_released = (soltar)

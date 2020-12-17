from gpiozero import DistanceSensor
import time
import sqlite3

ultrasonic = DistanceSensor(echo=21, trigger=20)


def ObjetoC():
    while True:
        distancia = ultrasonic.distance * 100
        if distancia > 20:
            print("Esperando objeto")
            time.sleep(1)
        else:
            fecha_1 = time.ctime()
            print("{:.4f}".format(distancia) + " cm")
            time.sleep(0.5)
            ultrasonic.wait_for_out_of_range()
            ObjetoR(fecha_1, distancia)


def ObjetoR(fecha_1, distancia):
    fecha_2 = time.ctime()
    time.sleep(0.1)
    datos = [(fecha_1, fecha_2, distancia)]
    conexion(datos)


def conexion(datos):
    conexion = sqlite3.connect('Ultrasonido.db')
    c = conexion.cursor()
    c.executemany(
        "insert into acciones (fecha_1,fecha_2,distancia) values(?,?,?)", datos)
    conexion.commit()
    conexion.close()


while True:
    ultrasonic.wait_for_in_range = (ObjetoC())

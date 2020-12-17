# Hacer un script que cuando se presione un botón, obtenga la
# fecha del sistema y guarde la acción, lo mismo debe hacer
# cuando se suelta el botón. Los registros deben quedar guardados
# en una BDD
import sqlite3

conexion = sqlite3.connect('Fecha.db')

c = conexion.cursor()

c.execute('''create table acciones (id_registro integer primary key autoincrement not null, verificador text, fecha text)''')

conexion.close()

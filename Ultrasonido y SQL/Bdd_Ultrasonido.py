import sqlite3

conexion = sqlite3.connect('Ultrasonido.db')

c = conexion.cursor()

c.execute('''create table acciones (id_registro integer primary key autoincrement not null, 
fecha_1 text not null, fecha_2 text not null, distancia float not null)''')

conexion.commit()

conexion.close()
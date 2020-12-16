import sqlite3


class Conectar:
    nombre_db = 'bdd/Bdd.db'

    def run_db(self, query, parametros=()):
        with sqlite3.connect(self.nombre_db) as conexion:
            cursor = conexion.cursor()
            datos = cursor.execute(query, parametros)

            conexion.commit()
        return datos

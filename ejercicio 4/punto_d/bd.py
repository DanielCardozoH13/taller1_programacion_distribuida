import mysql.connector
from mysql.connector import errorcode


class BaseDatos():
    def __init__(self, datos):
        try:
            host = datos[0]
            user = datos[1]
            passw = datos[2]
            bd = datos[3]
            self.conexion = mysql.connector.connect(user=user, password=passw, host=host, database=bd)
            self.cursor = self.conexion.cursor()
            print("\nConexión exitosa a la base de datos: " + bd + "\n")
            self.bandera = True
        except mysql.connector.Error as err:
            self.bandera = False
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\nHay algún problema con el usuario o la contraseña\n")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("\nLa Base de Datos no existe\n")
            else:
                print(err)

    def consultar_tablas(self):
        try:
            self.cursor.execute("SHOW TABLES")
            if self.cursor.with_rows:
                print("\nSe encontraron los siguientes elementos:", end="\n")
            for table in self.cursor:
                if self.cursor.with_rows:
                    print(table)
        except:
            print("hubo un error")

    def consultar_registros(self, query):
        try:
            self.cursor.execute(query)
            if self.cursor.with_rows:
                print("\nSe encontraron los siguientes elementos:", end="\n")
                print(self.cursor.column_names)
            for row in self.cursor:
                if self.cursor.with_rows:
                    print(row)
        except:
            print("\nhubo un error")

    def insertar_regi(self, datos):
        try:
            sql = "INSERT INTO tabla_prueba (nombre, apellido, correo, celular) VALUES ('" + datos[0] + "','" + datos[
                1] + "','" + datos[2] + "','" + datos[3] + "')"
            self.cursor.execute(sql)
            self.conexion.commit()
            print(self.cursor.rowcount, "Registro guardado")

        except:
            print("hubo un error")

    def actualizar_registro(self, id_tabla):
        try:
            sql = "SELECT * FROM tabla_prueba WHERE id_tabla = '" + id_tabla + "'"
            self.cursor.execute(sql)
            i = 0
            for row in self.cursor:
                for dato in row:
                    if i > 0:
                        print("  {}. {}".format(i,dato))
                    i = i+1
            opcion_mod = int(input('Seleccione el dato que desea modificar >> '))
            new_dato=input("ingrese el nuevo dato >> ")
            sentencia="UPDATE tabla_prueba SET "
            if opcion_mod == 1:
                field="nombre"
            elif opcion_mod == 2:
                field="apellido"
            elif opcion_mod == 3:
                field="correo"
            elif opcion_mod == 4:
                field="celular"
                while len(new_dato) != 10:
                    new_dato = input("ingrese un número correcto >> ")
            sql = sentencia+field+" = '"+new_dato+"' where id_tabla = '"+id_tabla+"'"
            self.cursor.execute(sql)
            self.conexion.commit()
            print(self.cursor.rowcount, "Registro actualizado")
        except:
            print("\nHubo un problema...")

    def eliminar_registro(self, id_tabla):
        try:
            sql="DELETE FROM `tabla_prueba` WHERE id_tabla = '"+id_tabla+"'"
            self.cursor.execute(sql)
            self.conexion.commit()
            print(self.cursor.rowcount, "Registro Eliminado")
        except:
            print("Hubo un problema...")

    def cerrar_conn(self):
        self.conexion.close()
        self.bandera = False

import mysql.connector

# Definir la conexión global
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oracle",
    database="tallerinvestigacion"
)

print("Conexión exitosa a la base de datos")

# Función para insertar líneas de investigación
def insertar_linea_investigacion(conexion, id, clave, titulo, linea, tipo, empresa):
    cursor = conexion.cursor()
    query = """INSERT INTO Proyectos (id, clave, titulo, linea_investigacion, tipo, empresa_institucion)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    datos = (id, clave, titulo, linea, tipo, empresa)
    cursor.execute(query, datos)
    conexion.commit()
    print("Línea de investigación creada correctamente.")

# Llamar a la función
insertar_linea_investigacion(conexion, 24, '2402-24', 'Nuevo proyecto', 'Nueva línea', 'DT', 'Institución X')

# Cerrar la conexión después de ejecutar todas las operaciones
conexion.close()
print("Conexión cerrada")

def insertar_linea_investigacion(conexion, id, clave, titulo, linea, tipo, empresa):
    cursor = conexion.cursor()
    query = """INSERT INTO Proyectos (id, clave, titulo, linea_investigacion, tipo, empresa_institucion)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    datos = (id, clave, titulo, linea, tipo, empresa)
    cursor.execute(query, datos)
    conexion.commit()
    print("Línea de investigación creada correctamente.")

insertar_linea_investigacion(conexion, 24, '2402-24', 'Nuevo proyecto', 'Nueva línea', 'DT', 'Institución X')

def consultar_lineas_investigacion(conexion):
    cursor = conexion.cursor()
    query = "SELECT linea_investigacion FROM Proyectos"
    cursor.execute(query)
    lineas = cursor.fetchall()
    for linea in lineas:
        print(linea)

consultar_lineas_investigacion(conexion)

def actualizar_linea_investigacion(conexion, vieja_linea, nueva_linea):
    cursor = conexion.cursor()
    query = """UPDATE Proyectos
               SET linea_investigacion = %s
               WHERE linea_investigacion = %s"""
    cursor.execute(query, (nueva_linea, vieja_linea))
    conexion.commit()
    print("Línea de investigación actualizada correctamente.")

    actualizar_linea_investigacion(conexion, 'RCISP', 'Nueva línea actualizada')

def eliminar_linea_investigacion(conexion, linea_a_eliminar):
    cursor = conexion.cursor()
    query = "DELETE FROM Proyectos WHERE linea_investigacion = %s"
    cursor.execute(query, (linea_a_eliminar,))
    conexion.commit()
    print("Línea de investigación eliminada correctamente.")

eliminar_linea_investigacion(conexion, 'Nueva línea actualizada')


import mysql.connector

# Definir la conexión global
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oracle",
    database="tallerinvestigacion"
)

print("Conexión exitosa a la base de datos")

# Crear un nuevo profesor
def crear_profesor(nombre, email, telefono):
    sql = "INSERT INTO Profesor (nombre, email, telefono) VALUES (%s, %s, %s)"
    valores = (nombre, email, telefono)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor {nombre} añadido con éxito.")

# Leer todos los profesores
def leer_profesores():
    sql = "SELECT * FROM Profesor"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for profesor in resultados:
        print(profesor)

# Actualizar un profesor
def actualizar_profesor(id_profesor, nombre, email, telefono):
    sql = "UPDATE Profesor SET nombre=%s, email=%s, telefono=%s WHERE id=%s"
    valores = (nombre, email, telefono, id_profesor)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor con ID {id_profesor} actualizado con éxito.")

# Eliminar un profesor
def eliminar_profesor(id_profesor):
    sql = "DELETE FROM Profesor WHERE id=%s"
    valores = (id_profesor,)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor con ID {id_profesor} eliminado con éxito.")



# Función para Crear
def crear_tipo_proyecto(tipo):
    query = "INSERT INTO Tipos_Proyectos (tipo) VALUES (%s)"
    cursor.execute(query, (tipo,))
    conexion.commit()
    print("Tipo de proyecto creado exitosamente.")

# Función para Leer
def leer_tipos_proyecto():
    query = "SELECT * FROM Tipos_Proyectos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(f"ID: {fila[0]}, Tipo: {fila[1]}")

# Función para Actualizar
def actualizar_tipo_proyecto(id, nuevo_tipo):
    query = "UPDATE Tipos_Proyectos SET tipo = %s WHERE id = %s"
    cursor.execute(query, (nuevo_tipo, id))
    conexion.commit()
    print("Tipo de proyecto actualizado exitosamente.")

# Función para Eliminar
def eliminar_tipo_proyecto(id):
    query = "DELETE FROM Tipos_Proyectos WHERE id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    print("Tipo de proyecto eliminado exitosamente.")

# Ejemplo de uso
try:
    # Crear un nuevo tipo de proyecto
    crear_tipo_proyecto("Innovación")

    # Leer todos los tipos de proyecto
    print("Tipos de proyecto existentes:")
    leer_tipos_proyecto()

    # Actualizar un tipo de proyecto
    actualizar_tipo_proyecto(1, "Desarrollo e Innovación")

    # Eliminar un tipo de proyecto
    eliminar_tipo_proyecto(2)

    # Consultar nuevamente
    print("Tipos de proyecto después de las operaciones:")
    leer_tipos_proyecto()

except mysql.connector.Error as e:
    print(f"Error en la operación: {e}")
finally:
    cursor.close()
    conexion.close()


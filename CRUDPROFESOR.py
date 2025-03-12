import mysql.connector

# Definir la conexión global
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oracle",
    database="tallerinvestigacion"
)

cursor = conexion.cursor()
print("Conexión exitosa a la base de datos")

# Funciones para Profesores
def crear_profesor(nombre, email, telefono):
    sql = "INSERT INTO Profesor (nombre, email, telefono) VALUES (%s, %s, %s)"
    valores = (nombre, email, telefono)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor {nombre} añadido con éxito.")

def leer_profesores():
    sql = "SELECT * FROM Profesor"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for profesor in resultados:
        print(f"ID: {profesor[0]}, Nombre: {profesor[1]}, Email: {profesor[2]}, Teléfono: {profesor[3]}")

def actualizar_profesor(id_profesor, nombre, email, telefono):
    sql = "UPDATE Profesor SET nombre=%s, email=%s, telefono=%s WHERE id=%s"
    valores = (nombre, email, telefono, id_profesor)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor con ID {id_profesor} actualizado con éxito.")

def eliminar_profesor(id_profesor):
    sql = "DELETE FROM Profesor WHERE id=%s"
    valores = (id_profesor,)
    cursor.execute(sql, valores)
    conexion.commit()
    print(f"Profesor con ID {id_profesor} eliminado con éxito.")

# Funciones para Tipos de Proyecto
def crear_tipo_proyecto(tipo):
    query = "INSERT INTO Tipos_Proyectos (tipo) VALUES (%s)"
    cursor.execute(query, (tipo,))
    conexion.commit()
    print("Tipo de proyecto creado exitosamente.")

def leer_tipos_proyecto():
    query = "SELECT * FROM Tipos_Proyectos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(f"ID: {fila[0]}, Tipo: {fila[1]}")

def actualizar_tipo_proyecto(id, nuevo_tipo):
    query = "UPDATE Tipos_Proyectos SET tipo = %s WHERE id = %s"
    cursor.execute(query, (nuevo_tipo, id))
    conexion.commit()
    print("Tipo de proyecto actualizado exitosamente.")

def eliminar_tipo_proyecto(id):
    query = "DELETE FROM Tipos_Proyectos WHERE id = %s"
    cursor.execute(query, (id,))
    conexion.commit()
    print("Tipo de proyecto eliminado exitosamente.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Crear un profesor")
        print("2. Leer profesores")
        print("3. Actualizar un profesor")
        print("4. Eliminar un profesor")
        print("5. Crear un tipo de proyecto")
        print("6. Leer tipos de proyectos")
        print("7. Actualizar un tipo de proyecto")
        print("8. Eliminar un tipo de proyecto")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del profesor: ")
            email = input("Ingrese el email del profesor: ")
            telefono = input("Ingrese el teléfono del profesor: ")
            crear_profesor(nombre, email, telefono)
        elif opcion == "2":
            print("Profesores existentes:")
            leer_profesores()
        elif opcion == "3":
            id_profesor = input("Ingrese el ID del profesor a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            actualizar_profesor(id_profesor, nombre, email, telefono)
        elif opcion == "4":
            id_profesor = input("Ingrese el ID del profesor a eliminar: ")
            eliminar_profesor(id_profesor)
        elif opcion == "5":
            tipo = input("Ingrese el tipo de proyecto: ")
            crear_tipo_proyecto(tipo)
        elif opcion == "6":
            print("Tipos de proyecto existentes:")
            leer_tipos_proyecto()
        elif opcion == "7":
            id = input("Ingrese el ID del tipo de proyecto a actualizar: ")
            nuevo_tipo = input("Ingrese el nuevo tipo de proyecto: ")
            actualizar_tipo_proyecto(id, nuevo_tipo)
        elif opcion == "8":
            id = input("Ingrese el ID del tipo de proyecto a eliminar: ")
            eliminar_tipo_proyecto(id)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del menú
try:
    menu()
except mysql.connector.Error as e:
    print(f"Error en la operación: {e}")
finally:
    cursor.close()
    conexion.close()

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

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Crear un tipo de proyecto")
        print("2. Leer tipos de proyectos")
        print("3. Actualizar un tipo de proyecto")
        print("4. Eliminar un tipo de proyecto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tipo = input("Ingrese el tipo de proyecto: ")
            crear_tipo_proyecto(tipo)
        elif opcion == "2":
            print("Tipos de proyecto existentes:")
            leer_tipos_proyecto()
        elif opcion == "3":
            id = input("Ingrese el ID del tipo de proyecto a actualizar: ")
            nuevo_tipo = input("Ingrese el nuevo tipo de proyecto: ")
            actualizar_tipo_proyecto(id, nuevo_tipo)
        elif opcion == "4":
            id = input("Ingrese el ID del tipo de proyecto a eliminar: ")
            eliminar_tipo_proyecto(id)
        elif opcion == "5":
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

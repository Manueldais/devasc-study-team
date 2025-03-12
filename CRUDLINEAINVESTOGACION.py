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

# Funciones CRUD para líneas de investigación
def insertar_linea_investigacion(id, clave, titulo, linea, tipo, empresa):
    query = """INSERT INTO Proyectos (id, clave, titulo, linea_investigacion, tipo, empresa_institucion)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    datos = (id, clave, titulo, linea, tipo, empresa)
    cursor.execute(query, datos)
    conexion.commit()
    print("Línea de investigación creada correctamente.")

def consultar_lineas_investigacion():
    query = "SELECT * FROM Proyectos"
    cursor.execute(query)
    lineas = cursor.fetchall()
    for linea in lineas:
        print(f"ID: {linea[0]}, Clave: {linea[1]}, Título: {linea[2]}, Línea: {linea[3]}, Tipo: {linea[4]}, Empresa: {linea[5]}")

def actualizar_linea_investigacion(vieja_linea, nueva_linea):
    query = """UPDATE Proyectos
               SET linea_investigacion = %s
               WHERE linea_investigacion = %s"""
    cursor.execute(query, (nueva_linea, vieja_linea))
    conexion.commit()
    print("Línea de investigación actualizada correctamente.")

def eliminar_linea_investigacion(linea_a_eliminar):
    query = "DELETE FROM Proyectos WHERE linea_investigacion = %s"
    cursor.execute(query, (linea_a_eliminar,))
    conexion.commit()
    print("Línea de investigación eliminada correctamente.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú CRUD Líneas de Investigación ---")
        print("1. Insertar una línea de investigación")
        print("2. Consultar líneas de investigación")
        print("3. Actualizar una línea de investigación")
        print("4. Eliminar una línea de investigación")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID: ")
            clave = input("Ingrese la clave: ")
            titulo = input("Ingrese el título: ")
            linea = input("Ingrese la línea de investigación: ")
            tipo = input("Ingrese el tipo: ")
            empresa = input("Ingrese la empresa o institución: ")
            insertar_linea_investigacion(id, clave, titulo, linea, tipo, empresa)
        elif opcion == "2":
            print("Líneas de investigación existentes:")
            consultar_lineas_investigacion()
        elif opcion == "3":
            vieja_linea = input("Ingrese la línea de investigación a actualizar: ")
            nueva_linea = input("Ingrese la nueva línea de investigación: ")
            actualizar_linea_investigacion(vieja_linea, nueva_linea)
        elif opcion == "4":
            linea_a_eliminar = input("Ingrese la línea de investigación a eliminar: ")
            eliminar_linea_investigacion(linea_a_eliminar)
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

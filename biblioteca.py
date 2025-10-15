import mysql.connector
from datetime import datetime

# =========================
# Clase de conexión a MySQL
# =========================
class ConexionBD:
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Toor",  # Cambiar por la contraseña de tu MySQL
                database="biblioteca"
            )
            self.cursor = self.conexion.cursor(dictionary=True)
            print("Conexión exitosa a la base de datos.")
        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")

    def ejecutar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        self.conexion.commit()

    def consultar(self, query, valores=None):
        self.cursor.execute(query, valores or ())
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conexion.close()

# =========================
# Clase Libro
# =========================
class Libro:
    def __init__(self, titulo, autor, anio, disponible=True):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = disponible

    # Getters y Setters
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible

# =========================
# Clase Usuario
# =========================
class Usuario:
    def __init__(self, nombre, tipo):
        self.__nombre = nombre
        self.__tipo = tipo

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

# =========================
# Clase Prestamo
# =========================
class Prestamo:
    def __init__(self, id_usuario, id_libro, fecha_prestamo, fecha_devolucion=None):
        self.__id_usuario = id_usuario
        self.__id_libro = id_libro
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion

    def get_id_usuario(self):
        return self.__id_usuario

    def get_id_libro(self):
        return self.__id_libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

# =========================
# Funciones del Sistema
# =========================
def registrar_libro(conexion, libro):
    conexion.ejecutar(
        "INSERT INTO libros (titulo, autor, anio, disponible) VALUES (%s, %s, %s, %s)",
        (libro.get_titulo(), libro.get_autor(), libro.get_anio(), libro.get_disponible())
    )
    print("Libro registrado correctamente.")

def registrar_usuario(conexion, usuario):
    conexion.ejecutar(
        "INSERT INTO usuarios (nombre, tipo) VALUES (%s, %s)",
        (usuario.get_nombre(), usuario.get_tipo())
    )
    print("Usuario registrado correctamente.")

def registrar_prestamo(conexion, prestamo):
    # Verificar disponibilidad del libro
    libro = conexion.consultar("SELECT * FROM libros WHERE id=%s", (prestamo.get_id_libro(),))
    if not libro:
        print("Libro no encontrado.")
        return
    if not libro[0]['disponible']:
        print("El libro no está disponible.")
        return

    # Registrar préstamo y actualizar disponibilidad
    conexion.ejecutar(
        "INSERT INTO prestamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)",
        (prestamo.get_id_usuario(), prestamo.get_id_libro(), prestamo.get_fecha_prestamo(), prestamo.get_fecha_devolucion())
    )
    conexion.ejecutar("UPDATE libros SET disponible = FALSE WHERE id = %s", (prestamo.get_id_libro(),))
    print("Préstamo registrado correctamente.")

def devolver_libro(conexion, id_prestamo):
    prestamo = conexion.consultar("SELECT * FROM prestamos WHERE id=%s", (id_prestamo,))
    if not prestamo:
        print("Préstamo no encontrado.")
        return

    conexion.ejecutar("UPDATE prestamos SET fecha_devolucion = %s WHERE id = %s", (datetime.now().date(), id_prestamo))
    conexion.ejecutar("UPDATE libros SET disponible = TRUE WHERE id = %s", (prestamo[0]['id_libro'],))
    print("Libro devuelto correctamente.")

def listar_libros(conexion):
    libros = conexion.consultar("SELECT * FROM libros")
    for libro in libros:
        estado = "Disponible" if libro['disponible'] else "Prestado"
        print(f"[{libro['id']}] {libro['titulo']} - {libro['autor']} ({libro['anio']}) -> {estado}")

def listar_prestamos(conexion):
    prestamos = conexion.consultar("SELECT * FROM prestamos")
    for p in prestamos:
        print(f"Préstamo ID: {p['id']} | Usuario ID: {p['id_usuario']} | Libro ID: {p['id_libro']} | Prestado: {p['fecha_prestamo']} | Devuelto: {p['fecha_devolucion']}")

# =========================
# Interfaz por Terminal
# =========================
def menu():
    conexion = ConexionBD()
    while True:
        print("""\n===== SISTEMA DE BIBLIOTECA =====
1. Registrar Libro
2. Registrar Usuario
3. Registrar Préstamo
4. Devolver Libro
5. Listar Libros
6. Listar Préstamos
0. Salir
================================
""")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = int(input("Año: "))
            registrar_libro(conexion, Libro(titulo, autor, anio))

        elif opcion == '2':
            nombre = input("Nombre del usuario: ")
            tipo = input("Tipo (Estudiante/Profesor): ")
            registrar_usuario(conexion, Usuario(nombre, tipo))

        elif opcion == '3':
            id_usuario = int(input("ID Usuario: "))
            id_libro = int(input("ID Libro: "))
            registrar_prestamo(conexion, Prestamo(id_usuario, id_libro, datetime.now().date()))

        elif opcion == '4':
            id_prestamo = int(input("ID del préstamo a devolver: "))
            devolver_libro(conexion, id_prestamo)

        elif opcion == '5':
            listar_libros(conexion)

        elif opcion == '6':
            listar_prestamos(conexion)

        elif opcion == '0':
            conexion.cerrar()
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

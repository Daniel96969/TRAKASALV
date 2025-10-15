Sistema de Biblioteca

README para el archivo biblioteca.py.

Descripción

Aplicación de consola en Python para gestionar una biblioteca mínima que permite:

Registrar libros.

Registrar usuarios.

Registrar préstamos y devoluciones.

Listar libros y préstamos.

El programa usa MySQL como backend para persistencia de datos.

Requisitos

Python 3.8+ (recomendado)

MySQL (servidor en local o remoto)

Paquete Python: mysql-connector-python

Instalación del paquete necesario:

pip install mysql-connector-python
Configuración de la base de datos

Crear la base de datos biblioteca en MySQL:

CREATE DATABASE biblioteca;
USE biblioteca;

Crear las tablas necesarias (ejemplo):

CREATE TABLE libros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  anio INT,
  disponible TINYINT(1) DEFAULT 1
);


CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  tipo VARCHAR(50) -- por ejemplo: Estudiante, Profesor
);


CREATE TABLE prestamos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  id_libro INT NOT NULL,
  fecha_prestamo DATE NOT NULL,
  fecha_devolucion DATE DEFAULT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE,
  FOREIGN KEY (id_libro) REFERENCES libros(id) ON DELETE CASCADE
);

Nota: ajusta los tipos y restricciones según tus necesidades.

Configurar credenciales

En biblioteca.py por defecto la conexión está configurada así:

self.conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Toor",  # Cambia por la contraseña de tu MySQL
    database="biblioteca"
)

Cambia host, user, password y database para que coincidan con tu entorno.

Sugerencia: para mayor seguridad, carga credenciales desde variables de entorno o un archivo de configuración en lugar de hardcodearlas.

Uso

Ejecuta el script desde la terminal:

python biblioteca.py

Verás un menú interactivo con opciones para registrar libros, usuarios, préstamos, devoluciones y listar datos.

Flujo básico

Registrar un libro (Título, Autor, Año).

Registrar un usuario (Nombre, Tipo).

Registrar préstamo (proporcionar ID de usuario y ID de libro).

Devolver un libro (proporcionar ID del préstamo).

Listar libros o préstamos para ver el estado.

Estructura del código

ConexionBD — Clase encargada de la conexión y ejecución de consultas. Métodos principales:

ejecutar(query, valores=None): ejecuta queries que modifican la BD.

consultar(query, valores=None): ejecuta queries SELECT y retorna resultados.

cerrar(): cierra cursor y conexión.

Libro — Clase modelo para libros (título, autor, año, disponible).

Usuario — Clase modelo para usuarios (nombre, tipo).

Prestamo — Clase modelo para préstamos (id_usuario, id_libro, fecha_prestamo, fecha_devolucion).

Funciones utilitarias:

registrar_libro(conexion, libro)

registrar_usuario(conexion, usuario)

registrar_prestamo(conexion, prestamo)

devolver_libro(conexion, id_prestamo)

listar_libros(conexion)

listar_prestamos(conexion)

menu() — Interfaz de consola que orquesta la ejecución.

Buenas prácticas y mejoras sugeridas

Manejar mejor los errores y excepciones (por ejemplo envolver ejecutar y consultar en try/except).

Validaciones de entrada (evitar conversiones que rompan el programa si el usuario ingresa texto donde se espera un número).

Reemplazar credenciales hardcodeadas por variables de entorno (os.environ) o un archivo .env.

Agregar logging en lugar de print para tener trazabilidad.

Implementar un pequeño CLI con argparse o click para ejecutar operaciones directamente sin el menú interactivo.

Añadir paginación/ordenamiento en listados si la base de datos crece.

Ejemplo rápido

Ejecutar el script.

Seleccionar 1 para registrar un libro.

Seleccionar 2 para registrar un usuario.

Seleccionar 3 para registrar un préstamo con los IDs correspondientes.

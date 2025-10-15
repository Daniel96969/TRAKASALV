# 📚 Sistema de Biblioteca — Proyecto en Python y MySQL

Este proyecto implementa un sistema de gestión de biblioteca simple en consola usando Python y MySQL. Permite registrar libros, usuarios, préstamos y devoluciones de manera eficiente.

🧩 Características principales

✅ Registrar libros con título, autor y año.

✅ Registrar usuarios (por ejemplo, estudiantes o profesores).

✅ Registrar préstamos y devoluciones.

✅ Listar todos los libros o préstamos activos.

✅ Conexión a base de datos MySQL para almacenamiento persistente.

⚙️ Requisitos

Python 3.8 o superior

MySQL instalado y corriendo localmente o en un servidor.

Librería Python:

pip install mysql-connector-python
🗃️ Configuración de la Base de Datos

Crea la base de datos:

CREATE DATABASE biblioteca;
USE biblioteca;

Crea las tablas necesarias:

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
  tipo VARCHAR(50)
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
🔐 Configuración de conexión

Dentro del archivo biblioteca.py, asegúrate de editar los datos de conexión:

self.conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Toor",  # ⚠️ Cambia esta contraseña
    database="biblioteca"
)

💡 Recomendado: usa variables de entorno o un archivo .env para mayor seguridad.

🚀 Ejecución del programa

Ejecuta el archivo principal desde la terminal:

python biblioteca.py

Se mostrará un menú interactivo con opciones como:

1️⃣ Registrar libro
2️⃣ Registrar usuario
3️⃣ Registrar préstamo
4️⃣ Registrar devolución
5️⃣ Listar libros
6️⃣ Listar préstamos
7️⃣ Salir

🧱 Estructura del código
📂 biblioteca.py
│
├── class ConexionBD      → Maneja la conexión con MySQL
├── class Libro           → Representa un libro en la biblioteca
├── class Usuario         → Representa un usuario (nombre, tipo)
├── class Prestamo        → Representa un préstamo de libro
│
├── registrar_libro()     → Inserta libros nuevos
├── registrar_usuario()   → Inserta usuarios nuevos
├── registrar_prestamo()  → Registra préstamos
├── devolver_libro()      → Marca libros como devueltos
├── listar_libros()       → Muestra todos los libros
├── listar_prestamos()    → Muestra los préstamos
└── menu()                → Controla el flujo principal del programa
🧠 Mejores prácticas recomendadas

Manejar errores con try/except para mayor robustez.

Validar entradas del usuario.

Sustituir credenciales por variables de entorno (os.environ).

Agregar logs en vez de print() para auditoría.

Añadir soporte CLI con argparse o click.

🧩 Ejemplo rápido de uso
python biblioteca.py

📖 Ingresa 1 → Agrega un libro.

👤 Ingresa 2 → Agrega un usuario.

📦 Ingresa 3 → Crea un préstamo.

↩️ Ingresa 4 → Devuelve un libro.

📋 Ingresa 5 o 6 → Lista los registros.

# Proyecto: Books Database – Reading Tracker

## Descripción

Este proyecto consiste en una aplicación de línea de comandos desarrollada en Python que permite registrar y analizar hábitos de lectura utilizando una base de datos relacional en MySQL.

El sistema permite almacenar información sobre libros, autores y lecturas realizadas por el usuario. Además, proporciona herramientas de consulta para analizar estadísticas de lectura como el autor más leído, el género favorito o el número de libros leídos por año.

El objetivo del proyecto es practicar el diseño de bases de datos relacionales, el uso de consultas SQL y la integración de una base de datos con una aplicación en Python.

---

# Tecnologías utilizadas

* Python (aplicación principal y lógica del sistema)
* MySQL (gestión de base de datos)
* SQL (consultas y manipulación de datos)
* Git & GitHub 

---

# Arquitectura del proyecto

El proyecto sigue una estructura modular para separar responsabilidades.

```
books-database
│
├── src
│   ├── main.py
│   ├── database
│   │   └── conexion.py
│   ├── services
│   │   ├── consultas.py
│   │   └── agregar_datos.py
│   └── interface
│       └── cli.py
│
├── db
│   ├── schema.sql
│   ├── seed.sql
│   └── queries.sql
│
├── docs
│   ├── proyecto.md
│   └── database_diagram.png
│
├── requirements.txt
├── .gitignore
└── README.md
    
```

Cada módulo cumple una función específica dentro del sistema.

---

# Componentes del sistema

## main.py

Es el punto de entrada de la aplicación. Se encarga de iniciar el programa y ejecutar el menú principal de la interfaz CLI.

---

## cli.py

Contiene la interfaz de línea de comandos del sistema.
Permite al usuario interactuar con la aplicación a través de un menú con distintas opciones como:

* consultar libros
* registrar nuevas lecturas
* agregar autores o libros
* visualizar estadísticas

Este módulo dirige cada opción del menú hacia las funciones correspondientes.

---

## conexion.py

Define la función responsable de establecer la conexión con la base de datos MySQL.
Centralizar la conexión permite reutilizarla en distintos módulos sin repetir código.

---

## consultas.py

Contiene todas las funciones encargadas de realizar consultas a la base de datos.
Estas funciones utilizan principalmente sentencias SQL de tipo `SELECT`.

Ejemplos de consultas implementadas:

* obtener los libros mejor puntuados
* calcular el autor más leído
* determinar el género favorito
* listar libros leídos por año
* buscar libros por título

---

## agregar_datos.py

Contiene las funciones que modifican la base de datos.

Estas funciones utilizan sentencias SQL como:

* INSERT
* UPDATE
* DELETE

Permiten registrar nuevos libros, autores y lecturas en el sistema.

---

# Diseño de la base de datos

La base de datos está compuesta por tres tablas principales.

## Tabla autores

Almacena la información de los autores de los libros.

Campos principales:

* id_autor (clave primaria)
* nombre

---

## Tabla libros

Almacena los libros registrados en el sistema.

Campos principales:

* id_libro (clave primaria)
* titulo
* genero
* paginas
* id_autor (clave foránea que referencia a la tabla autores)

---

## Tabla lecturas

Registra cada lectura realizada por el usuario.

Campos principales:

* id_lectura (clave primaria)
* id_libro (clave foránea)
* fecha_inicio
* fecha_fin
* puntuacion
* comentario

---

# Relaciones entre tablas

El sistema utiliza relaciones entre tablas para evitar duplicación de datos.

* Un autor puede tener múltiples libros.
* Un libro puede tener múltiples registros de lectura.

Esto permite mantener la base de datos normalizada y facilita el análisis posterior de los datos.

---

# Funcionalidades principales

El sistema permite realizar las siguientes operaciones:

* registrar autores
* agregar libros
* registrar lecturas
* buscar libros por título
* consultar el autor más leído
* identificar el género favorito
* analizar estadísticas de lectura

---

# Posibles mejoras futuras

El proyecto puede expandirse con nuevas funcionalidades como:

* Recomendaciones de lectura
* Seguimiento de libros pendientes por leer
* Análisis de hábitos de lectura por año
* Visualización de estadísticas más avanzadas

---

# Objetivo del proyecto

Este proyecto fue desarrollado con el objetivo de practicar:

* Diseño de bases de datos relacionales
* Consultas SQL complejas
* Integración entre Python y MySQL
* Organización de proyectos de software

También sirve como proyecto de portfolio para demostrar conocimientos en bases de datos y desarrollo backend.

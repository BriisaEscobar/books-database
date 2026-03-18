# 📚 Books Database

Aplicación de consola desarrollada en Python para gestionar una base de datos de libros y lecturas personales.

## 🛠 Tecnologías utilizadas

* Python
* MySQL
* SQL
* Git & GitHub

## 🚀 Funcionalidades

* 🔎 Buscar libros por título
* ⭐ Ver el Top 5 de libros mejor puntuados
* 📊 Mostrar estadísticas de lectura
* ➕ Registrar nuevos libros
* 📖 Registrar lecturas con puntuación y comentario

## Ejemplo de estadísticas

El programa puede calcular:

- Libros mejor y peor valorados
- Libros leídos por año
- Autor más leído
- Calificación promedio

## 🗂 Estructura del proyecto
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

## ▶ Cómo ejecutar el proyecto

1. Clonar el repositorio git clone https://github.com/BriisaEscobar/books-database.git 

2. Configurar la conexión a la base de datos en database.py.

3. Ejecutar: python main.py

## 👩‍💻 Autor 

Brisa Escobar 

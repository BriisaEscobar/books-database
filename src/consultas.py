# agregar mas consultas 
from conexion import * 

def top_libros():
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT titulo, puntuacion
        FROM libros
        JOIN lecturas USING(id_libro)
        ORDER BY puntuacion DESC
        LIMIT 5
    """)
    
    for titulo, puntuacion in cursor:
        print(titulo, "-", puntuacion)

def libros_por_anio():
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT YEAR(fecha_fin), COUNT(*)
        FROM lecturas
        GROUP BY YEAR(fecha_fin)
    """)

    for anio, cantidad in cursor:
        print(anio, ":", cantidad)

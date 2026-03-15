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

# ----------------------------------------------

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

# ----------------------------------------------

def autor_mas_leido():
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute( """ 
                   SELECT autor.nombre, COUNT(*) AS Cantidad 
                   FROM autor 
                   JOIN libros USING(id_autor)
                   JOIN lecturas USING (id_libro)
                   GROUP BY autor.nombre 
                   ORDER BY cantidad DESC 
                   LIMIT 1
    """)
    resultado = cursor.fetchone()
    print("Autor mas leido: ", resultado)

# ----------------------------------------------

def genero_favorito(): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute(""" 
                    SELECT libros.genero, COUNT(*) AS Cantidad
                    FROM libros
                    JOIN lecturas USING (id_libro)
                    GROUP BY genero 
                    ORDER BY Cantidad DESC
                    LIMIT 1; 
    si lo hago sin limite me muestra todos pero deberia 
    filtrar los repetidos y estaria bueno
    """)
    genero = cursor.fetchone()

    print("Genero favorito es: ", genero)

# ----------------------------------------------

def libro_mas_largo():
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
            SELECT titulo,  paginas
            FROM lecturas
            JOIN libros USING (id_libro)
            GROUP BY paginas
            ORDER BY paginas DESC
            LIMIT 1;        
    """)

    libro = cursor.fetchone()
   
    print("Libro leido mas largo:", libro)

# ----------------------------------------------

def buscar_libro(unLibro):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute(""" 
            SELECT titulo 
            FROM libros 
            WHERE titulo LIKE %s 
    """ , ("%" + unLibro + "%",))
    
    resultado = cursor.fetchall() 

    for libro in resultado: 
        print(libro[0])
# mejorar la busqueda con el autor y el print resultado 
# el print que me devuelva todo id_libro, titulom genero autor y pags 

# ----------------------------------------------

def agregar_libro(id_libro, titulo, genero, id_autor, paginas):

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO libros (id_libro, titulo, genero, id_autor, paginas)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_libro, titulo, genero, id_autor,paginas))

    conexion.commit()

    print("Libro agregado correctamente")

# ----------------------------------------------


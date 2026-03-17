from database import obtenerConexion 

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

def buscar_libro(unLibro):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute(""" 
            SELECT libros.titulo, autor.nombre, libros.genero
            FROM libros 
            JOIN autor USING (id_autor)
            WHERE libros.titulo LIKE %s;
    """,  ("%" + unLibro + "%",))

    resultado = cursor.fetchall() 

    for titulo, autor, genero in resultado:
        print(titulo,"-", autor,"-", genero)

    if not resultado: 
        print("No se encontró el libro con ese título")

# ----------------------------------------------

def agregar_libro(id_libro, titulo, genero, id_autor, paginas):

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO libros (id_libro, titulo, genero, id_autor, paginas)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_libro, titulo, genero, id_autor,paginas))

    conexion.commit()

    print("Libro agregado correctamente :)")

# ----------------------------------------------

def estadisticas():

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    print("\n===== ESTADISTICAS DE LECTURA =====")

    cursor.execute("SELECT COUNT(*) FROM lecturas")
    total = cursor.fetchone()[0]
   
    print("Total libros leidos:", total)
    
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

    cursor.execute("SELECT AVG(puntuacion) FROM lecturas")
    promedio = cursor.fetchone()[0]
    print("Promedio de puntuacion:", round(promedio,2), "\n")

    cursor.execute("""
        SELECT titulo
        FROM libros
        JOIN lecturas USING(id_libro)
        ORDER BY puntuacion DESC
        LIMIT 1
    """)
    mejor = cursor.fetchone()
    if mejor:
        print("Libro mejor puntuado:", mejor[0])
        
    cursor.execute("""
        SELECT titulo
        FROM libros
        JOIN lecturas USING(id_libro)
        ORDER BY puntuacion ASC
        LIMIT 1
    """)
    peor = cursor.fetchone()
    if peor:
        print("Libro peor puntuado:", peor[0], "\n")
    
    
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
    print("Autor mas leido:", resultado)
   
    cursor.execute(""" 
                    SELECT libros.genero, COUNT(*) AS Cantidad
                    FROM libros
                    JOIN lecturas USING (id_libro)
                    GROUP BY genero 
                    ORDER BY Cantidad DESC
                    LIMIT 1; 
    """)
    genero = cursor.fetchone()

    print("Genero favorito es:", genero, "\n")

    cursor.execute("""
        SELECT YEAR(fecha_fin), COUNT(*)
        FROM lecturas
        GROUP BY YEAR(fecha_fin)
    """)

    for anio, cantidad in cursor:
        print("Libro leidos en: ", anio, ":", cantidad)

    print ("-----------------------------------------")
    
# ----------------------------------------------

def registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
            INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario))
    conexion.commit()

    print("Lectura registrada correctamente :)")

# ----------------------------------------------
  
def registrar_Autor(id_autor, nombre):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
            INSERT INTO autor(id_autor, nombre)
            VALUES (%s, %s)
        """), (id_autor, nombre)
    conexion.commit()
    print("Autor regist4rado correctamente :)")
    
    
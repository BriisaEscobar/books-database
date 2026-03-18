from database.conexion import obtenerConexion

def registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
            INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario))
    conexion.commit()

    print("Lectura registrada correctamente :)")

    cursor.close()
    conexion.close()

def agregar_libro_con_autor(titulo, genero, paginas, nombre_autor):

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_autor
        FROM autor
        WHERE nombre = %s
    """, (nombre_autor,))

    resultado = cursor.fetchone()

    if resultado:
        id_autor = resultado[0]
    else:
        cursor.execute("""
            INSERT INTO autor (nombre)
            VALUES (%s)
        """, (nombre_autor,))
        
        conexion.commit()
        id_autor = cursor.lastrowid

        print("Autor creado automáticamente :)")

    cursor.execute("""
        INSERT INTO libros (titulo, genero, paginas, id_autor)
        VALUES (%s, %s, %s, %s)
    """, (titulo, genero, paginas, id_autor))

    conexion.commit()

    print("Libro agregado correctamente :)")

    cursor.close()
    conexion.close()


   
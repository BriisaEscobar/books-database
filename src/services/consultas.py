from database.conexion import obtenerConexion 
from datetime import datetime

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

    print("TOP 5 mejores libros")

    for titulo, puntuacion in cursor:
        print("->", titulo, "-", puntuacion)
    
    cursor.close()
    conexion.close()

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

    cursor.close()
    conexion.close()

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

    cursor.close()
    conexion.close()

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
            GROUP BY titulo, paginas
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

    cursor.close()
    conexion.close()

    print ("-----------------------------------------")
    
# ----------------------------------------------

def registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    if not validar_fechas(fecha_inicio, fecha_fin): 
        return 
    
    if not validar_puntuacion(puntuacion):
        print("Puntuacion inválida [1-5]")
        return 

    if not validar_comentario(comentario):
        print("Comentario inválido")
        return 
    
    cursor.execute("""
            INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario))
    conexion.commit()

    print("Lectura registrada correctamente :)")

    cursor.close()
    conexion.close()

# ----------------------------------------------
  
def registrar_Autor(id_autor, nombre):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute("""
            INSERT INTO autor(id_autor, nombre)
            VALUES (%s, %s)
        """), (id_autor, nombre)
    conexion.commit()
    print("Autor registrado correctamente :)")

    cursor.close()
    conexion.close()

# ---------------------------------------------- 

def validar_fechas(fecha_inicio, fecha_fin):
    try: 
        inicio = datetime.strptime(fecha_inicio,"%Y-%m-%d")
        fin= datetime.strptime(fecha_fin, "%Y-%m-%d")

        if fin < inicio: 
            print("La fecha de fin no puede ser anterior a la de de inicio")
            return False
        return True
    
    except ValueError: 
        print("Formato de fecha inválido (YYYY-MM-DD)")
        return False 

# ---------------------------------------------- 

def validar_puntuacion(puntuacion): 
    try: 
        puntuacion = int(puntuacion)
        return 1 <= puntuacion <= 5 
    except: 
        return False 

# ---------------------------------------------- 
""" 
def validar_comentario(comentario): 
    validos = ["Excelente", "Muy bueno", "Bueno", "Regular" "Malo"]
    return comentario in validos
"""
# ----------------------------------------------   

def validar_estado(estado): 
    validos = ["Pendiente", "Leyendo", "Terminado", "Abandonado"]
    return estado in validos 

# ----------------------------------------------   

def terminar_lectura(id_lectura, puntuacion, comentario):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            SELECT fecha_inicio, estado
            FROM lecturas
            WHERE id_lectura = %s
        """, (id_lectura,))

        resultado = cursor.fetchone()

        if not resultado:
            print(f"No existe la lectura {id_lectura}")
            return

        fecha_inicio, estado_actual = resultado

        if estado_actual != "leyendo":
            print(f"No se puede terminar una lectura en estado {estado_actual}")
            return

        if not fecha_inicio:
            print("No tiene fecha de inicio")
            return
        
        if not (1 <= puntuacion <= 5):
            print("Puntuación inválida")
            return

        fecha_fin = datetime.now().date()

        if fecha_fin < fecha_inicio:
            print("Fechas incoherentes")
            return

        cursor.execute("""
            UPDATE lecturas
            SET estado          = %s,
                puntuacion      = %s,
                comentario      = %s,
                fecha_fin       = %s
            WHERE id_lectura    = %s
        """, ("terminado", puntuacion, comentario, fecha_fin, id_lectura))

        conexion.commit()

        print(f"Lectura finalizada correctamente el {fecha_fin}")

        if estado_actual == "Terminado": 
            resultado = input("Desea cambiar el comentario (y/n): ")

            if resultado == 'y':
                editar_comentario(id_lectura, nuevo_comentario)
                nuevo_comentario = input("Ingrese el nuevo comenatrio: ")
                agregar_historial_comentarios(nuevo_comentario, id_lectura)
                return 

            else:
                return print ("lectura terminada con comentario original")
                #tendria que hacre un validar respuesta y/n

    finally:
        cursor.close()
        conexion.close()

# ----------------------------------------------   

def editar_comentario(id_lectura, nuevo_comentario): 
    conexion = obtenerConexion 
    cursor = conexion.cursor()

    cursor.execute("""
            SELECT id_lectura, comentario
            FROM lecturas
            WHERE id_lectura = %s; 
        """, (id_lectura,))
    
    resultado = cursor.fetchone()

    if not resultado:
        print(f"No existe la lectura {id_lectura}")
        return

    cursor.execute(""" 
            UPDATE lecturas 
            SET comentario = %s
            WHERE id_lectura       
    """), (id_lectura, nuevo_comentario)
    
    conexion.commit()

    cursor.close()
    conexion.close()

# ----------------------------------------------   
def agregar_historial_comentarios(nuevo_comentario, id_lectura) :
    conexion = obtenerConexion()
    cursor = conexion.conexion()

    cursor.execute("""
            SELECT COUNT (*) 
            FROM historial_comentarios 
            WHERE id_lectura = %s
        """, (id_lectura,))

    total_cambios = cursor.fetchone()

    if total_cambios >=5: 
        print ("Has excedido el limite de cambios en el historial de comentarios ")
        return 

    cursor.execute("""
            UPDATE lecturas 
            SET comentario   = %s
            WHERE id_lectura = %s,                  
    """, (id_lectura,))

    resultado = cursor.fetchone()
    comentario_anterior = resultado[0] if resultado else None

    if comentario_anterior != nuevo_comentario: 
        cursor.execute("""
                UPDATE lecturas 
                SET comentario   = %s
                WHERE id_lectura = %s
        """, (nuevo_comentario, id_lectura))
    
    cursor.execute(""" 
            INSERT INTO historial_comentarios 
            (id_lectura, comentario_anterior, comentario_nuevo)
            LIMIT 5;
    """), (id_lectura, comentario_anterior, nuevo_comentario)
 
    conexion.commit()
    print("Comentario actualizado e historial guardado")

        


    





    



  


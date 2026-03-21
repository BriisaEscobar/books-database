from database.conexion import obtenerConexion 
from datetime import datetime
# TERMINADO
def top_libros():
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    try:    
        cursor.execute("""
            SELECT titulo, puntuacion
            FROM libros
            JOIN lecturas USING(id_libro)
            ORDER BY puntuacion DESC
            LIMIT 5
            """)
        
        resultado = cursor.fetchall()

        libros = []

        for titulo, puntuacion in resultado:
            libros.append({
                "titulo": titulo, 
                "puntuacion": puntuacion
            })

        return {
            "success": True, 
            "data": libros
        }
    
    except Exception as e: 
        return {
        "success": False, 
        "error": "ERROR:INTERNO",
        "detalle": str(e)
        }
        
    finally:        
        cursor.close()
        conexion.close()

# ----------------------------------------------
# TERMINADO

def buscar_libro(unLibro):
    conexion = obtenerConexion()
    cursor = conexion.cursor()
    try: 
        cursor.execute(""" 
            SELECT libros.titulo, autor.nombre, libros.genero
            FROM libros 
            JOIN autor USING (id_autor)
            WHERE libros.titulo LIKE %s;
            """,  ("%" + unLibro + "%",))

        resultado = cursor.fetchone() 
        if resultado: 
            titulo, autor, genero = resultado
            return{
                "success": True,
                "data": {
                    "titulo": titulo, 
                    "autor": autor, 
                    "genero": genero
                }
            }
        else: 
            return {
                "success": False, 
                "error": "NO_SE_ENCONTRO_LIBRO"
            }

    except Exception as e: 
        return {
        "success": False, 
        "error": "ERROR:INTERNO",
        "detalle": str(e)
        }
        
    finally:   
        cursor.close()
        conexion.close()

# ----------------------------------------------
"""
def agregar_libro(id_libro, titulo, genero, id_autor, paginas):

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute(
        INSERT INTO libros (id_libro, titulo, genero, id_autor, paginas)
        VALUES (%s, %s, %s, %s, %s)
    , (id_libro, titulo, genero, id_autor,paginas))

    conexion.commit()

    print("Libro agregado correctamente :)")

    cursor.close()
    conexion.close()
"""

# ----------------------------------------------
# TERMINADO
def estadisticas():

    conexion = obtenerConexion()
    cursor = conexion.cursor()

    try: 
        # total de libros leidos
        cursor.execute("SELECT COUNT(*) FROM lecturas")
        total = cursor.fetchone()[0]
        
        #libro mas largo 
        cursor.execute("""
            SELECT titulo,  paginas
            FROM lecturas
            JOIN libros USING (id_libro)
            GROUP BY titulo, paginas
            ORDER BY paginas DESC
            LIMIT 1;        
        """)

        libro = cursor.fetchone()
   
        # promedio de puntuacion 
        cursor.execute("SELECT AVG(puntuacion) FROM lecturas")

        promedio = cursor.fetchone()[0]

        # mejor puntaje
        cursor.execute("""
            SELECT titulo, puntuacion 
            FROM libros
            JOIN lecturas USING(id_libro)
            ORDER BY puntuacion DESC
            LIMIT 1
        """)

        mejor = cursor.fetchone()

        # peor puntaje
        cursor.execute("""
            SELECT titulo, puntuacion 
            FROM libros
            JOIN lecturas USING(id_libro)
            ORDER BY puntuacion ASC
            LIMIT 1
        """)
        peor = cursor.fetchone()

        #autor mas leido
        cursor.execute( """ 
            SELECT autor.nombre, COUNT(*) AS Cantidad 
            FROM autor 
            JOIN libros USING(id_autor)
            JOIN lecturas USING (id_libro)
            GROUP BY autor.nombre 
            ORDER BY cantidad DESC 
            LIMIT 1
        """)
        autor = cursor.fetchone()
       
        # genero favorito
        cursor.execute(""" 
            SELECT libros.genero, COUNT(*) AS Cantidad
            FROM libros
            JOIN lecturas USING (id_libro)
            GROUP BY genero 
            ORDER BY Cantidad DESC
            LIMIT 1; 
        """)
        genero = cursor.fetchone()

        #cantidad por anio
        cursor.execute("""
            SELECT YEAR(fecha_fin), COUNT(*)
            FROM lecturas
            GROUP BY YEAR(fecha_fin)
        """)

        anio= [{"anio": anio, "cantidad": cantidad}
               for anio, cantidad in cursor.fetchall()
        ]
        
        return {
        "success": True, 
        "data": {
            "total_leidos": total,
            "libro_mas_largo": {
                "titulo": libro[0], 
                "paginas": libro[1]
            } if libro else None, 

            "promedio_puntuacion": round(promedio, 2)
            if promedio else None, 

            "mejor_libro": {
                "nombre":mejor[0],
                "puntaje": mejor[1]
            } if mejor else None,

            "peor_libro": {
                "nombre": peor[0], 
                "puntaje": peor[1]
            }if peor else None,

            "autor_mas_leido":{
                "nombre": autor[0], 
                "cantidad": autor[1]
            } if autor else None, 

            "genero_favorito": {
                "genero": genero[0], 
                "cantidad": genero[1]
            } if genero else None,

            "lecturas_por_anio": anio
        }
    }

    except Exception as e:
        return {
            "success": False,
            "error": "ERROR_INTERNO",
            "detalle": str(e)
        }
    
    finally:
        cursor.close()
        conexion.close()
   
# ----------------------------------------------

def registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    if not validar_fechas(fecha_inicio, fecha_fin): 
        return 
    
    if not validar_puntuacion(puntuacion):
        print("Puntuacion inválida [1-5]")
        return 

    # not validar_comentario(comentario):
        #print("Comentario inválido")
        #return 
    
    cursor.execute("""
            INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario))
    conexion.commit()

    print("Lectura registrada correctamente :)")

    cursor.close()
    conexion.close()

# ----------------------------------------------
"""
def registrar_Autor(id_autor, nombre):
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    cursor.execute(
            INSERT INTO autor(id_autor, nombre)
            VALUES (%s, %s)
        ), (id_autor, nombre)
    conexion.commit()
    print("Autor registrado correctamente :)")

    cursor.close()
    conexion.close()
""" 

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

    finally:
        cursor.close()
        conexion.close()

# ----------------------------------------------   
# TERMINADO 

def editar_comentario(id_lectura, nuevo_comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    try:
        if not nuevo_comentario or nuevo_comentario.strip() == "":
            return {
            "success": False, 
            "error": "COMENTARIO_INVALIDO"
            }
        cursor.execute("""
            SELECT comentario, estado 
            FROM lecturas
            WHERE id_lectura = %s;      
        """, (id_lectura,))
    
        resultado = cursor.fetchone()

        if not resultado:
            return {
            "success" : False, 
            "error"    : "LECTURA_NO_EXISTE"   
            }

        comentario_anterior, estado_actual = resultado

        if estado_actual != "terminado": 
            return {
                "success": False,
                "error": "LECTURA_NO_TERMINADA"
            }
    
        if comentario_anterior == nuevo_comentario:
            return {
            "succes" : False,
            "error"  : "SIN_CAMBIOS"
            }

        cursor.execute ("""
            INSERT INTO historial_comentarios 
            (id_lectura, comentario_anterior, nuevo_comentario)
            VALUES (%s, %s, %s)
            """, (id_lectura, comentario_anterior, nuevo_comentario))
    
        cursor.execute(""" 
            UPDATE lecturas 
            SET comentario = %s
            WHERE id_lectura = %s    
            """, (nuevo_comentario, id_lectura))

        conexion.commit()

        return {
        "success": True, 
        "data": {
            "id_lectura": id_lectura,
            "comentario_anterior": comentario_anterior, 
            "comentario_nuevo": nuevo_comentario
        }
    }
    
    except Exception as e:
        conexion.rollback()
        return {
            "success": False, 
            "error": "ERROR_INTERNO", 
            "details": str(e)
        }
    
    finally:
        cursor.close()
        conexion.close()

# ----------------------------------------------   

        


    





    



  


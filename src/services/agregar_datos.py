from database.conexion import obtenerConexion
from datetime import datetime

# TERMINADO

def registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario): 
    conexion = obtenerConexion()
    cursor = conexion.cursor()

    try: 
        if not validar_fechas(fecha_inicio, fecha_fin): 
            return {
            "success": False, 
            "error": "FECHAS_INVALIDAS"
        }
    
        if not validar_puntuacion(puntuacion):
            return {
                "success": False, 
                "error": "PUNTUACION_INVALIDA"
            }

        else: 
            cursor.execute("""
            INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            VALUES (%s, %s, %s, %s, %s)
            """, (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario))
        
        conexion.commit()

        return {
            "success": True, 
            "data": {
                "id_libro": id_libro, 
                "fecha_inicio": fecha_inicio, 
                "fecha_fin": fecha_fin, 
                "puntuacion": puntuacion, 
                "comentario": comentario
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

def agregar_libro_con_autor(titulo, genero, paginas, nombre_autor):

    conexion = obtenerConexion()
    cursor = conexion.cursor()
    try: 
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

        cursor.execute("""
            INSERT INTO libros (titulo, genero, paginas, id_autor)
            VALUES (%s, %s, %s, %s)
        """, (titulo, genero, paginas, id_autor))

        conexion.commit()

        return {
                "success": True, 
                "data": {
                    "titulo": titulo, 
                    "genero": genero, 
                    "paginas": paginas, 
                    "autor": nombre_autor
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

def validar_puntuacion(puntuacion): 
    try: 
        puntuacion = int(puntuacion)
        return 1 <= puntuacion <= 5 
    except: 
        return False 

# ----------------------------------------------   

def validar_estado(estado): 
    validos = ["Pendiente", "Leyendo", "Terminado", "Abandonado"]
    return estado in validos 

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
   
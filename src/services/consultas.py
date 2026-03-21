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
# TERMINADO

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
            return {
                "success": False, 
                "error": "NO_EXISTE_LA_LECTURA"
            }
        
        fecha_inicio, estado_actual = resultado

        if estado_actual != "leyendo":
            return {
                "success": False, 
                "error": "ERROR_ESTADO"
            }
           

        if not fecha_inicio:
            return {
                "success": False, 
                "error": "NO_TIENE_FECHA_INICIO"
            }
        
        if not (1 <= puntuacion <= 5):
            print("Puntuación inválida")
            return {
                "success": False, 
                "error": "PUNTUACION_INVALIDA"                
            }
      
        fecha_fin = datetime.now().date()

        if fecha_fin < fecha_inicio:
            return {
                "success": False, 
                "error": "FECHAS_INCOHERENTES"
            }

        cursor.execute("""
            UPDATE lecturas
            SET estado          = %s,
                puntuacion      = %s,
                comentario      = %s,
                fecha_fin       = %s
            WHERE id_lectura    = %s
        """, ("terminado", puntuacion, comentario, fecha_fin, id_lectura))

        conexion.commit()

        return {
            "succes": True, 
            "data": {
                "estado": "terminado", 
                "puntuacion": puntuacion, 
                "comentario": comentario, 
                "fecha fin" : fecha_fin, 
                "id lectura": id_lectura
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

    
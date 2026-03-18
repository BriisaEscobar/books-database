from database.conexion import obtenerConexion 
import services.consultas as consultas
import services.agregar_datos as agregar 
def menu():
    while True:

        print("\n===== PROYECT-BOOKS DATABASE =====")
        print("1 - Top 5 mejores libros")
        print("2 - Buscar libro")
        print("3 - Estadísticas")
        print("4 - Registrar libro")
        print("5 - Registrar lectura")
        print("6 - Registrar autor")
        print("n - Salir")
       
        opcion = input("Seleccione opcion: ") #print("\n") QUIERO UN SALTO DE LINEA 

        if opcion == "1":
            consultas.top_libros()

        elif opcion == "2":
           titulo = input("Ingrese el titulo del libro: ")
           consultas.buscar_libro(titulo) 

        elif opcion == "3":
            consultas.estadisticas()

        # corregir esto ahora va agregar libro con autor!!
        elif opcion == "4":
            id_libro = input("Id del libro: ")
            titulo   = input("Titulo del libro: ")
            genero   = input("Género del libro: ")
            id_autor = input("Id autor: ")
            paginas  = input("Páginas del libro: ")
            agregar.agregar_libro(id_libro, titulo, genero, id_autor, paginas)

        elif opcion =="5":
            id_libro     = input("Id del libro: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin    = input("fecha de fin (YYYY-MM-DD): ")
            puntuacion   = input("Puntuacion del libro [1-5]: ")
            comentario   = input("Comentario del libro (Exelente, Muy bueno, Bueno, Regular, Malo): ")

            agregar.registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
            
            
        elif opcion == "6":
            break 

        else: 
            print("Opcion inválida")

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
        print("7 - Terminar lectura")
        print("8 - Editar comentario")
        print("n - Salir")
       
        opcion = input("Seleccione opcion: ") 

        # TOP LIBROS 
        if opcion == "1":
            resultado = consultas.top_libros() 
            
            if resultado["success"]: 
                print("\nTOP 5 mejores libros")
                for libro in resultado["data"]: 
                    print(f"-> {libro["titulo"]} {libro['puntuacion']}")
            else: 
                print("Error", resultado["error"])

        # BUSCAR LIBRO
        elif opcion == "2":
           
            titulo = input("Ingrese el titulo del libro: ")
            resultado = consultas.buscar_libro(titulo) 
            
            if resultado["success"]: 
               libro = resultado["data"]

               print("\n📚 Libro encontrado:")
               print("titulo:", libro["titulo"])
               print("autor:", libro["autor"])
               print("genero:", libro["genero"])

            else:
                print("Error:", resultado["error"])

        # ESTADISICAS
        elif opcion == "3": 
            resultado = consultas.estadisticas()

            if resultado["success"]: 
                data = resultado["data"]
            
                print("\n===== ESTADISTICAS DE LECTURA =====")
                print("Total de libros leidos: ", data["total_leidos"])

                if data["libro_mas_largo"]:
                    print("Libro mas largo leido", data["libro_mas_largo"]["titulo"], 
                    "-", data["libro_mas_largo"]["paginas"], "paginas")

                print("Promedio de puntuacion: "), data["promedio_puntuacion"]

                if data["mejor_libro"]: 
                    print("Mejor libro:", data["mejor_libro"]["nombre"], "-" , data["mejor_libro"]["puntaje"])

                if data["peor_libro"]:
                    print("Peor libro:", data["peor_libro"]["nombre"], "-", data["peor_libro"]["puntaje"])

                if data ["autor_mas_leido"]:
                    print("Autor favorito", data["autor_mas_leido"]["nombre"], "-", data["autor_mas_leido"] ["cantidad"])
                
                if data ["genero_favorito"]:
                    print("Genero favorito", data["genero_favorito"]["genero"])
                
                print("\nLibros por año:")
                for item in data["lecturas_por_anio"]:
                    print(item["anio"], ":", item["cantidad"])

            else: 
                print("Error:",resultado["error"])           


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
            
        # reviusar opcion 6 

        elif opcion == "7": 
            id_lectura = input("Ingrese el Id de la lectura: ")
            puntuacion = int(input("Ingrese una puntuacion al libro: "))
            comentario = input("Ingrese un comentario sobre el libro: ")
            
            consultas.terminar_lectura(id_lectura, puntuacion, comentario)

        elif opcion == "8":
            id_lectura = input("Ingrese el Id de la lectura: ")
            nuevo_comentario = input("Ingrese el nuevo comentario: ")

            consultas.editar_comentario(id_lectura, nuevo_comentario)


        elif opcion == "n":
            print("Saliendo del sistema...")
            break 

        else: 
            print("Opcion inválida")()


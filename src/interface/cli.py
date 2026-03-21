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
        print("6 - Terminar lectura")
        print("7 - Editar comentario")
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
            
                print("\n 📚 ===== ESTADISTICAS DE LECTURA ===== 📚 ")
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

            
        # REGISTAR LIBRO CON AUTOR
        elif opcion == "4":
    
            titulo   = input("Titulo del libro: ")
            genero   = input("Género del libro: ")
            paginas  = int(input("Páginas del libro: "))
            autor    = input("Autor del libro: ")

            resultado = agregar.agregar_libro_con_autor(titulo, genero, paginas,autor)

            if resultado["success"]: 
                data = resultado["data"]
                
                print("\n 📚 ===== LIBRO REGISTRADO ===== 📚 ")
                print("Titulo:", data["titulo"])
                print("Autor:", data["autor"])
                print("Género:", data["genero"])
                print("Páginas:", data["paginas"])
    


            else: 
                print("Error:", resultado["error"])

        # REGISTRAR LECTURA 
        elif opcion =="5":
            id_libro = input ("ID del libro: ")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
            puntuacion = int(input("Puntuación: "))
            comentario = input("Comentario: ")            

            resultado = agregar.registrar_Lectura(id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)

            if resultado["success"]: 
                data = resultado["data"]

                print("\n 📚 ===== LECTURA REGISTRADA ===== 📚")

                if data["id_libro"]: {
                    print("Id del libro:", data["id_libro"])
                }
                    
                if data["fecha_inicio"]: 
                    print("Fecha de inicio: ", data["fecha_inicio"])

                if data["fecha_fin"]: 
                    print("Fecha de fin: ", data["fecha_fin"])

                if data["puntuacion"]: 
                    print("Puntuacion: ", data["puntuacion"])
                
                if data["comentario"]: 
                    print("Comentario: " ,data["comentario"])
         
            else: 
                print("Error:", resultado["error"])

        # TERMINAR LECTURA
        elif opcion == "6": 
            id_lectura = input("Ingrese el Id de la lectura: ")
            puntuacion = int(input("Ingrese una puntuacion al libro: "))
            comentario = input("Ingrese un comentario sobre el libro: ")
            
            consultas.terminar_lectura(id_lectura, puntuacion, comentario)

            if resultado["success"]: 
                data = resultado["data"]

                print("\n 📚 ===== LECTURA REGISTRADA ===== 📚")

                if data["id_lectura"]: {
                    print("Id lectura:", data["id_lectura"])
                }

                if data["puntuacion"]: 
                    print("Puntuacion: ", data["puntuacion"])
                
                if data["comentario"]: 
                    print("Comentario: " ,data["comentario"])
         
            else: 
                print("Error:", resultado["error"])

        # EDITAR COMENTARIO 
        elif opcion == "7":
            id_lectura = input("Ingrese el Id de la lectura: ")
            nuevo_comentario = input("Ingrese el nuevo comentario: ")

            resultado = consultas.editar_comentario(id_lectura, nuevo_comentario)

            if resultado["success"]: 
                data = resultado["data"]

                if ["id_lectura"]: 
                    print(["id_lectura"], data["id_lectura"])
                
                if ["comentario_anterior"]:
                    print(["comentario_anterior"], data["comentario_anterior"])
                
                if ["comentario_nuevo"]: 
                    print(["comentario_nuevo"], data["comentario_nuevo"])

        # SALIR 
        elif opcion == "n":
            print("Saliendo del sistema...")
            break 

        else: 
            print("Opcion inválida")


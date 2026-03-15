# agregar mas opciones 
# interfaz 
from consultas import * 
from agregar_datos import * 

def menu():
    while True:

        print("\n===== PROYECT-BOOKS DATABASE =====")
        print("1 - Top 5 mejores libros")
        print("2 - Libros leídos por año")
        print("3 - Autor más leído")
        print("4 - Género favorito")
        print("5 - Libro leído más largo")
        print("6 - Buscar libro")
        print("7 - Agregar libro")
        print("8 - Salir")
       
        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            top_libros()

        elif opcion == "2":
            libros_por_anio()

        elif opcion == "3":
            autor_mas_leido()
        
        elif opcion == "4":
            genero_favorito()

        elif opcion == "5":
            libro_mas_largo()

        elif opcion == "6":
            titulo = input("Ingrese el titulo del libro:")
            buscar_libro(titulo) 

        elif opcion == "7":
            id_libro = input("Id del libro: ")
            titulo   = input("Titulo del libro: ")
            genero   = input("Género del libro: ")
            id_autor = input("Id autor: ")
            paginas  = input("Páginas del libro: ")
            agregar_libro(id_libro, titulo, genero, id_autor, paginas)


        elif opcion == "8":
            break 

        else: 
            print("Opcion inválida")

""" 
opciones de consultas para hacer:
-> buscar libro (terminar y mejorar)
-> estadisticas de lectura tambien con promedio de puntuaciones promedio de lectura
-> registar autor o lectura 
""" 

# TERMINADOS Y PROBADOS
# top 5 mejores libros 
# libros leidos por año (cantidad)
# autor mas leido 
# genero favorito 
# libro mas largo leido 
# agregar libro 
# salir

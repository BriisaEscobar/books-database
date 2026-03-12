# agregar mas opciones 
# interfaz 
from consultas import * 
from agregar_datos import * 

def menu():
    while True:

        print("\n===== PROYECT-BOOKS DATABASE =====")
        print("1 - Top libros")
        print("2 - Libros leidos por año")
        print("3 - Salir")
       
        opcion = input("Seleccione opcion: ")

        if opcion == "1":
            top_libros()

        elif opcion == "2":
            libros_por_anio()

        elif opcion == "3":
            break 

""" 
opciones de consultas para hacer:
-> top libros 
-> libros leidos por año 
-> autor mas leido 
-> promedio de puntuaciones 
-> libro mas largo leido 
-> tiempo promedio de lectura 
-> buscar libro 
-> estadisticas de lectura 
-> genero fav 

""" 
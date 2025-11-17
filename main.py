'''
Esta app pretende ser una prueba de desarrollo en la que muestro mis conocimientos sobre Python, utilizando y renovando lo que vaya aprendiendo a través del curso de Python
'''
import gestionPeliculas
from pelicula import Pelicula



def mostrarMenu():
    op = -1
    while(op != 5):
        print("--------------MENÚ OPCIONES-----------\n",
            "1.Mostrar películas\n",
            "2.Buscar películas\n",
            "3.Añadir película\n",
            "5.Salir")
        op = int(input("Selecciona una opción: "))

        match(op):
            case 1:
                gestionPeliculas.listarPeliculas(LISTA_PELICULAS)
            case 2:
                texto = "s"
                while texto != "n" and texto != "N":
                    texto = input("Buscar: ")
                    gestionPeliculas.buscarPelicula(texto)
                    texto = input("¿Continuar buscando? S/N")
            case 3:
                gestionPeliculas.crearPelicula()
    else:
        print("Hasta pronto!")





#FUNCION A EJECUTAR
mostrarMenu()






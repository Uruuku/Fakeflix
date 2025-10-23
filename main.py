'''
Esta app pretende ser una prueba de desarrollo en la que muestro mis conocimientos sobre Python, utilizando y renovando lo que vaya aprendiendo a través del curso de Python
'''


#Lo primero que debe hacer nuestro programa de peliculas es contar con peliculas

LISTA_PELICULAS = [
    {
        "titulo" : "titulo1",
        "sinopsis" : "blablabla",
        "duracion" : 120,
        "fecha_estreno" : "12/12/2012",
        "genero" : "accion",
        "actores" : ("actor1", "actor2", "actor3", "actor4"),
        "director" : "director1",
        "productora" : "empresa1",
        "valoracion" : 4.5,
        "comentarios" : {
            "idcomentario1":("usuario1", "Me parece increible la pelicula blablabla1", "valoracion1"),
            "idcomentario2":("usuario2", "Me parece increible la pelicula blablabla2", "valoracion2"),
            "idcomentario3":("usuario3", "Me parece increible la pelicula blablabla3", "valoracion3")
        }
    },
    {
        "titulo" : "titulo2",
        "sinopsis" : "blablabla",
        "duracion" : 120,
        "fecha_estreno" : "12/12/2012",
        "genero" : "terror",
        "actores" : ("actor1", "actor2", "actor3", "actor4"),
        "director" : "director2",
        "productora" : "empresa2",
        "valoracion" : 4.5,
        "comentarios" : {
            "idcomentario1":("usuario1", "Me parece increible la pelicula blablabla1", "valoracion1"),
            "idcomentario2":("usuario2", "Me parece increible la pelicula blablabla2", "valoracion2"),
            "idcomentario3":("usuario3", "Me parece increible la pelicula blablabla3", "valoracion3")
        }
    },
    {
        "titulo" : "titulo3",
        "sinopsis" : "blablabla",
        "duracion" : 120,
        "fecha_estreno" : "12/12/2012",
        "genero" : "accion",
        "actores" : ("actor1", "actor2", "actor3", "actor4"),
        "director" : "director3",
        "productora" : "empresa3",
        "valoracion" : 4.5,
        "comentarios" : {
            "idcomentario1":("usuario1", "Me parece increible la pelicula blablabla1", "valoracion1"),
            "idcomentario2":("usuario2", "Me parece increible la pelicula blablabla2", "valoracion2"),
            "idcomentario3":("usuario3", "Me parece increible la pelicula blablabla3", "valoracion3")
        }
    }
]




def buscarPelicula(texto):
    pelis = []
    for pelicula in LISTA_PELICULAS:
        if(texto in pelicula['titulo'] or texto in pelicula['director'] or texto in pelicula['genero']):
            pelis.append(pelicula)
    
    if(len(pelis) > 0):
        listarPeliculas(pelis)            
    else:
        print("No se encontró ninguna película")


def listarTitulosPeliculas(peliculas):
    print("-----LISTA DE PELICULAS-----")
    for np, pelicula in peliculas:
        print(f'Titulo: {pelicula["titulo"]}')
    

def listarPeliculas(peliculas):

    print("---------------------ULTIMAS PELICULAS---------------------")
    for pelicula in peliculas:
        for key,value in pelicula.items():
            if isinstance(value, dict):
                for k,v in value.items():
                    print(f'{k} : {v}')
            elif isinstance(value, tuple):
                for v in range(len(value)):
                    print(f'{key}{v+1} : {value[v]}')
            else:
                print(f'{key} : {value}')
        print("-------------------------------------------------------------\n")



def mostrarMenu():
    op = -1
    while(op != 5):
        print("--------------MENÚ OPCIONES-----------\n",
            "1.Mostrar películas\n",
            "2.Buscar películas\n",
            "5.Salir")
        op = int(input("Selecciona una opción: "))

        match(op):
            case 1:
                listarTitulosPeliculas(LISTA_PELICULAS)
            case 2:
                texto = input("Buscar: ")
                buscarPelicula(texto)
    else:
        print("Hasta pronto!")





#CODIGO A EJECUTAR
mostrarMenu()






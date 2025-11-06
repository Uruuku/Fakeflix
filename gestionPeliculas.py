plantilla_peliculas = {
    "titulo" : "",
    "sinopsis" : "",
    "duracion" : 0,
    "fecha_estreno" : "12//2012",
    "genero" : "acion",
    "actores" : [],
    "director" : "",
    "productora" : "",
    "valoracion" : 0,
    "comentarios" : {}
}

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
        "actores" : ["actor1", "actor2", "actor3", "actor4"],
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

def crearPelicula():
    pelicula = plantilla_peliculas.copy()
    pelicula['titulo'] = input("Introduce título de la película ")
    pelicula['sinpopsis'] = input("Introduce la sinopsis de la película ")
    pelicula['duracion'] = input("Introduce la duración de la película ")
    pelicula['fecha_estreno'] = input("Introduce la fecha de estreno de la película ")
    pelicula['genero'] = input("Introduce el genero de la pelicula ")
    
    actor = input("Introduce el nombre de los actores del reparto separados por comas o introdúcelos uno a uno ")
    if len(actor.split(";")) > 1:
        pelicula['actores'] = actor.split(";")
    else:
        pelicula['actores'].append(actor)
    
    while input("¿Quieres añadir más? S/N").upper() != "N":
        pelicula['actores'].append(input("Introduce el nombre del actor "))

    pelicula['director'] = input("Introduce el nombre del director ")
    pelicula['productora'] = input("Introduce el nombre de la productora ")

    LISTA_PELICULAS.append(pelicula)




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
    for np, pelicula in peliculas.items():
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
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

def crear_pelicula():
    print("\n--- Nueva Película ---")
    
    # 1. Recolección y limpieza básica de datos (strip elimina espacios extra)
    titulo = input("Introduce título de la película: ").strip()
    sinopsis = input("Introduce la sinopsis: ").strip()
    
    # 2. Validación de tipo de dato (Duración debe ser entero)
    while True:
        try:
            duracion_input = input("Introduce la duración (minutos): ")
            duracion = int(duracion_input)
            break
        except ValueError:
            print("❌ Por favor, introduce un número válido para la duración.")

    fecha_estreno = input("Introduce la fecha de estreno (DD/MM/AAAA): ").strip()
    genero = input("Introduce el género: ").strip()
    
    # 3. Lógica de actores optimizada (List Comprehension)
    # Se permite introducir todo de una vez separado por comas
    actores_input = input("Introduce los actores (separados por comas): ")
    # Esto divide por comas y limpia espacios alrededor de cada nombre
    lista_actores = [actor.strip() for actor in actores_input.split(',') if actor.strip()]

    director = input("Introduce el director: ").strip()
    productora = input("Introduce la productora: ").strip()

    # 4. Construcción del diccionario
    nueva_pelicula = {
        "titulo": titulo,
        "sinopsis": sinopsis,
        "duracion": duracion,
        "fecha_estreno": fecha_estreno,
        "genero": genero,
        "actores": lista_actores, # Guardamos como lista para poder editar luego
        "director": director,
        "productora": productora,
        "valoracion": 0.0, # Valor por defecto
        "comentarios": {}  # Diccionario vacío por defecto
    }

    # 5. Actualización de la lista global
    LISTA_PELICULAS.append(nueva_pelicula)
    print(f"✅ Película '{titulo}' añadida con éxito.")





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
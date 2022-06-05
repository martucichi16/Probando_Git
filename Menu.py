from Artistas import Musico

camila_cabello = Musico("Camila Cabello",
                        [{"nombre": "Familia", "cant_canciones": 12, "publicacion": 2022, "duracion": "34 min, 20 seg"},
                         {"nombre": "Romance", "cant_canciones": 14, "publicacion": 2019, "duracion": "46 min, 47 seg"},
                         {"nombre": "Camila", "cant_canciones": 11, "publicacion": 2018, "duracion": "37 min"}],
                        ["Havana", "Señorita", "Bam bam", "Never be the same", "Dont go yet"],
                        "Pop", "Solista")

the_beatles = Musico("The Beatles",
                     [{"nombre": "Let it be", "cant_canciones": 12, "publicacion": 1970, "duracion": "35 min, 10 seg"},
                      {"nombre": "Abbey Road", "cant_canciones": 17, "publicacion": 1969, "duracion": "47 min, 29 seg"},
                      {"nombre": "Help!", "cant_canciones": 14, "publicacion": 1965, "duracion": "33 min, 55 seg"}],
                     ["Here comes the sun", "Come togheter", "Let it be", "Yesterday", "Hey Jude", "Blackbird", "Help"],
                     "Rock & Roll", "Banda")

billy_joel = Musico("Billy Joel",
                    [{"nombre": "The stranger", "cant_canciones": 9, "publicacion": 1977, "duracion": "42 min, 33 seg"},
                     {"nombre": "Piano man", "cant_canciones": 10, "publicacion": 1973, "duracion": "43 min, 17 seg"}],
                    ["Uptown girl", "Piano Man", "Moovin Out", "Vienna", "We didnt start the fire"],
                    "Pop/Rock/Jazz", "Solista")

olivia_rodrigo = Musico("Olivia Rodrigo",
                  [{"nombre": "SOUR", "cant_canciones": 11, "publicacion": 2021, "duracion": "34 min, 46 seg"}],
                  ["Drivers licence", "Good 4 u", "Traitor", "Deja vu"], "Pop", "Solista")


musicos = [camila_cabello, the_beatles, billy_joel, olivia_rodrigo]

def menu():
    print("Bienvenido a la base de datos de artistas")

    while True:
        print("Por favor elija una de las siguentes opciones")
        print("1) Solicitar informacion de la base de datos")
        print("2) Agregar informacion de un nuevo artista")

        option = input(">> ")

        if option == "1":
            while True:
                num = 1
                for musico in musicos:
                    print(f"{num}) {musico.nombre}")
                    num += 1

                print(f"{len(musicos) + 1}) Salir")

                option_2 = input(">> ")

                if option_2 == str((len(musicos) + 1)):
                    break

                else:
                    artista = musicos[int(option_2) - 1]
                    while True:
                        print("Informacion solicitable")
                        print("1) Descricion general")
                        print("2) Enlistar canciones más conocidas")
                        print("3) Buscar un album en especifico")
                        print("Si quiere salir ingrese \"quit\"")

                        option_3 = input(">> ")

                        if option_3 == "1":
                            artista.descripcion()

                        elif option_3 == "2":
                            artista.canciones_conocidas()

                        elif option_3 == "3":
                            album = input("Ingrese el album a buscar: ")
                            artista.describir_album(album)

                        elif option_3 == "quit":
                            break

                        else:
                            print("Opcion no valida")

        elif option == "2":
            print("Ingrese la informacion solicitada a continuacion con respecto al nuevo artista a gregar")
            nombre = input("Nombre: ")

            print("~Albumes~")
            albumes = []

            while True:
                print("1) Agregar album")
                print("2) Continuar con el resto de la informacion")

                option_4 = input(">> ")

                if option_4 == "1":
                    nombre_album = input("Ingrede nombre del album: ")
                    cant_canciones = input("Cantidad de canciones: ")
                    publicacion = input("Año de publicacion: ")
                    duracion = input("Duracion total del album: ")

                    album = {"nombre": nombre_album, "cant_canciones": cant_canciones, "publicacion": publicacion,
                             "duracion": duracion}

                    albumes.append(album)

                elif option_4 == "2":
                    break

            print("~Canciones conocidas~")

            canciones = []

            while True:
                cancion = input("Ingrese una cancion (al terminar ingrese salir): ")

                if cancion != "salir":
                    canciones.append(cancion)

                elif cancion == "salir":
                    break

            estilo_musical = input("Estilo musical: ")
            tipo_musico = input("¿Solista o banda? ")

            musicos.append(Musico(nombre, albumes, canciones, estilo_musical, tipo_musico))

        else:
            break


menu()

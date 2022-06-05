class Musico:

    def __init__(self, nombre, albumes, top_canciones, estilo_musical, tipo_musico):
        self.nombre = nombre
        self.albumes = albumes
        self.top_canciones = top_canciones
        self.estilo_musical = estilo_musical
        self.tipo_musico = tipo_musico

    def describir_album(self, album_buscado):
        for album in self.albumes:
            if album["nombre"] == album_buscado:
                print(f"~~~ {album['nombre'].upper()} ~~~"
                      f"\nCantidad de canciones: {str(album['cant_canciones'])}"
                      f"\nAño de publicacion: {str(album['publicacion'])}"
                      f"\nDuracion total: {album['duracion']}")
                
    def canciones_conocidas(self):
        num = 1
        print(f"TOP {len(self.top_canciones)} CANCIONES MAS POPULARES")
        for cancion in self.top_canciones:
            print(f"{num}) {cancion}")
            num += 1

    def descripcion(self):
        print(f"El/La {self.tipo_musico.lower()} {self.nombre} toca musica del genero {self.estilo_musical}")

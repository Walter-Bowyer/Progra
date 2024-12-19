import json
import os
class Libro:
    contador_consecutivo = 1

    def __init__(self, titulo, autor, anio_publicacion, numero_de_volumen=1):
        """
        Función que contiene la información de los libros
        """
        self.consecutivo = Libro.contador_consecutivo
        Libro.contador_consecutivo += 1
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True
        self.numero_de_volumen = numero_de_volumen
    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.anio_publicacion})"
    

    def to_dict(self):
            """Convierte el objeto libro a un diccionario."""
            return {
                "consecutivo": self.consecutivo,
                "titulo": self.titulo,
                "autor": self.autor,
                "anio_publicacion": self.anio_publicacion,
                "disponible": self.disponible,
                "numero_de_volumen": self.numero_de_volumen
            }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto libro desde un diccionario."""
        libro = cls(data["titulo"], data["autor"], data["anio_publicacion"], data["numero_de_volumen"])
        libro.consecutivo = data["consecutivo"]
        libro.disponible = data["disponible"]
        return libro


class Usuario:
    def __init__(self, nombre, id_usuario):
        """
        Esta función contine la info del usuario
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []


    def to_dict(self):
            """Convierte el objeto usuario a un diccionario."""
            return {
                "nombre": self.nombre,
                "id_usuario": self.id_usuario,
                "libros_prestados": [libro.consecutivo for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto usuario desde un diccionario y guarda el consecutivo de los libros prestados."""
        usuario = cls(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = data["libros_prestados"] 
        return usuario
    
    
class Biblioteca:
    def __init__(self, archivo_libros="data/libros.json", archivo_usuarios="data/usuarios.json"):
        self.libros = []
        self.usuarios = []
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.cargar_datos()

    def registrar_libro(self, libro):
        # Agrega los libros a la lista
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        # Registra nuevos usuarios a la biblioteca
        self.usuarios.append(usuario)

    def prestar_libro(self, titulo, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                break
        else:
            # Imprime un mensaje si el usuario no está registrado
            return f"El usuario con ID {id_usuario} no está registrado."
            # Realiza una busqueda para ver si el libro esta y si, sí lo esta verifica si esta disponible
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                usuario.libros_prestados.append(libro)
                # Imprime un mensaje si el libro se presto a un usuario
                return f"El libro '{titulo}' ha sido prestado a {usuario.nombre}."
        # Verifica si el libro está en la biblioteca pero no está disponible
        for libro in self.libros:
            if libro.titulo == titulo:
                return f"El libro '{titulo}' no está disponible."
        # Imprime un mensaje si el libro no se encuentra en la biblioteca
        return f"El libro '{titulo}' no se encuentra en la biblioteca."

    def devolver_libro(self, titulo, id_usuario):
        # Busca al usuario por ID
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                break
        else:
            # Imprime un mensaje si el usuario no está registrado
            return f"El usuario con ID {id_usuario} no está registrado."

        # Busca el libro en la lista de libros prestados del usuario
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                libro.disponible = True
                usuario.libros_prestados.remove(libro)
                # Imprime un mensaje si ellibro ya se devolvio y quien lo devolvio
                return f"El libro '{titulo}' ha sido devuelto por {usuario.nombre}."
        # Imprime un mensaje si el libro no está en los libros prestados del usuario
        return f"El usuario {usuario.nombre} no tiene el libro '{titulo}'."

    def mostrar_libros_disponibles(self):
        # Devuelve una lista de los libros disponibles
        return [str(libro) for libro in self.libros if libro.disponible]

    def mostrar_usuarios(self):
        # devuelve una lista de los usuarios registrados
        return [f"{usuario.nombre} (ID: {usuario.id_usuario})" for usuario in self.usuarios]

    def guardar_datos(self):
        """Guarda la información de libros y usuarios en archivos .json"""
        with open(self.archivo_libros, "w", encoding="utf-8") as libros_file:
            json.dump([libro.to_dict() for libro in self.libros], libros_file, ensure_ascii=False, indent=4)
        
        with open(self.archivo_usuarios, "w", encoding="utf-8") as usuarios_file:
            json.dump([usuario.to_dict() for usuario in self.usuarios], usuarios_file, ensure_ascii=False, indent=4)
    
    def cargar_datos(self):
        """Carga la información de libros y usuarios desde archivos .json"""
        if os.path.exists(self.archivo_libros):
            with open(self.archivo_libros, "r", encoding="utf-8") as libros_file:
                libros_data = json.load(libros_file)
                self.libros = [Libro.from_dict(data) for data in libros_data]

        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "r", encoding="utf-8") as usuarios_file:
                usuarios_data = json.load(usuarios_file)
                for data in usuarios_data:
                    usuario = Usuario.from_dict(data)
                    # Asignar los libros prestados a los usuarios
                    for consecutivo in usuario.libros_prestados:
                        libro = next((lib for lib in self.libros if lib.consecutivo == consecutivo), None)
                        if libro:
                            usuario.libros_prestados.append(libro)
                            libro.disponible = False
                    self.usuarios.append(usuario)
    
    
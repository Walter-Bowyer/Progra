import os
import json

class ManejadorErrores:
    def __init__(self, archivo_libros, archivo_usuarios):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.libros = []  # Asegúrate de inicializar la lista de libros
        self.usuarios = []  # Asegúrate de inicializar la lista de usuarios

    def validar_usuario_existente(self, usuarios, id_usuario):
        for u in usuarios:
            if u.id_usuario == id_usuario:
                return f"El ID de usuario {id_usuario} ya está registrado."
        return None

    def validar_usuario_no_registrado(self, usuarios, id_usuario):
        for u in usuarios:
            if u.id_usuario == id_usuario:
                return u
        return f"El usuario con ID {id_usuario} no está registrado."
    
    def validar_libro_disponible(self, libros, titulo):
        for l in libros:
            if l.titulo == titulo and l.disponible:
                return l
        return f"El libro '{titulo}' no existe o no está disponible."
    
    def validar_libro_prestado(self, usuario, titulo):
        for l in usuario.libros_prestados:
            if l.titulo == titulo:
                return l
        return f"El usuario {usuario.nombre} no tiene el libro '{titulo}'."

    def guardar_datos(self):
        # Guarda la información de libros y usuarios en archivos .json
        if not os.path.exists(os.path.dirname(self.archivo_libros)) or not os.path.exists(os.path.dirname(self.archivo_usuarios)):
            print("Error: La carpeta 'data' no existe. Por favor, créala en la raíz del proyecto.")
            return

        # Guarda libros
        with open(self.archivo_libros, "w", encoding="utf-8") as libros_file:
            json.dump([libro.to_dict() for libro in self.libros], libros_file, ensure_ascii=False, indent=4)

        # Guarda usuarios
        with open(self.archivo_usuarios, "w", encoding="utf-8") as usuarios_file:
            json.dump([usuario.to_dict() for usuario in self.usuarios], usuarios_file, ensure_ascii=False, indent=4)

        print("Datos guardados correctamente.")
        
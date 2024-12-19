import json
import os
from Biblioteca.clases import Libro, Usuario

def cargar_datos(ruta_libros, ruta_usuarios):
    """Carga los datos de libros y usuarios desde archivos .json"""
    libros = []
    usuarios = []

    if os.path.exists(ruta_libros):
        with open(ruta_libros, "r", encoding="utf-8") as libros_file:
            libros_data = json.load(libros_file)
            libros = [Libro.from_dict(data) for data in libros_data]

    if os.path.exists(ruta_usuarios):
        with open(ruta_usuarios, "r", encoding="utf-8") as usuarios_file:
            usuarios_data = json.load(usuarios_file)
            usuarios = [Usuario.from_dict(data) for data in usuarios_data]

    return libros, usuarios
def guardar_datos(ruta_libros, ruta_usuarios, libros, usuarios):
    """Guarda los datos de libros y usuarios en archivos .json"""
    with open(ruta_libros, "w", encoding="utf-8") as libros_file:
        json.dump([libro.to_dict() for libro in libros], libros_file, ensure_ascii=False, indent=4)

    with open(ruta_usuarios, "w", encoding="utf-8") as usuarios_file:
        json.dump([usuario.to_dict() for usuario in usuarios], usuarios_file, ensure_ascii=False, indent=4)

from Biblioteca.clases import Biblioteca, Libro, Usuario

def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n--- Menú de Biblioteca Virtual ---")
    print("1. Registrar un libro")
    print("2. Registrar un usuario")
    print("3. Prestar un libro")
    print("4. Devolver un libro")
    print("5. Ver lista de libros disponibles")
    print("6. Ver lista de usuarios")
    print("7. Salir")

def registrar_libro(biblioteca):
    print("\n--- Registrar un Libro ---")
    while True:
        print("Escribe 'SALIR' en cualquier momento para regresar al menú principal.")
        titulo = input("Ingresa el título del libro: ")
        if titulo.upper() == "SALIR":
            break
        autor = input("Ingresa el autor del libro: ")
        if autor.upper() == "SALIR":
            break
        try:
            anio_publicacion = int(input("Ingresa el año de publicación: "))
        except ValueError:
            print("Año inválido. Intenta de nuevo.")
            continue
        if str(anio_publicacion).upper() == "SALIR":
            break
        numero_de_volumen = input("Ingresa el número de volumen: ")
        if numero_de_volumen.upper() == "SALIR":
            break
        try:
            numero_de_volumen = int(numero_de_volumen)
        except ValueError:
            print("Número de volumen inválido. Intenta de nuevo.")
            continue

        libro = Libro(titulo, autor, anio_publicacion, numero_de_volumen)
        biblioteca.registrar_libro(libro)
        biblioteca.guardar_datos()
        print(f"Libro '{titulo}' registrado exitosamente.")
        break  # Regresa al menú principal después del registro

def registrar_usuario(biblioteca):
    print("\n--- Registrar un Usuario ---")
    while True:
        print("Escribe 'SALIR' en cualquier momento para regresar al menú principal.")
        nombre = input("Ingresa el nombre del usuario: ")
        if nombre.upper() == "SALIR":
            break
        id_usuario = input("Ingresa el ID del usuario (número único): ")
        if id_usuario.upper() == "SALIR":
            break
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            print("ID inválido. Debe ser un número. Intenta de nuevo.")
            continue

        if any(u.id_usuario == id_usuario for u in biblioteca.usuarios):
            print(f"Error: El ID {id_usuario} ya está registrado.")
            continue
        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)
        biblioteca.guardar_datos()
        print(f"Usuario '{nombre}' registrado exitosamente.")
        break  # Regresa al menú principal después del registro

def prestar_libro(biblioteca):
    print("\n--- Prestar un Libro ---")
    while True:
        print("Escribe 'SALIR' en cualquier momento para regresar al menú principal.")
        titulo = input("Ingresa el título del libro a prestar: ")
        if titulo.upper() == "SALIR":
            break
        id_usuario = input("Ingresa el ID del usuario: ")
        if id_usuario.upper() == "SALIR":
            break
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            print("ID inválido. Intenta de nuevo.")
            continue

        mensaje = biblioteca.prestar_libro(titulo, id_usuario)
        print(mensaje)
        biblioteca.guardar_datos()
        break

def devolver_libro(biblioteca):
    print("\n--- Devolver un Libro ---")
    while True:
        print("Escribe 'SALIR' en cualquier momento para regresar al menú principal.")
        titulo = input("Ingresa el título del libro a devolver: ")
        if titulo.upper() == "SALIR":
            break
        id_usuario = input("Ingresa el ID del usuario: ")
        if id_usuario.upper() == "SALIR":
            break
        try:
            id_usuario = int(id_usuario)
        except ValueError:
            print("ID inválido. Intenta de nuevo.")
            continue

        mensaje = biblioteca.devolver_libro(titulo, id_usuario)
        print(mensaje)
        biblioteca.guardar_datos()
        break

def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    biblioteca = Biblioteca(archivo_libros="data/libros.json", archivo_usuarios="data/usuarios.json")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            registrar_libro(biblioteca)

        elif opcion == "2":
            registrar_usuario(biblioteca)

        elif opcion == "3":
            print("Función: Prestar un libro.")

        elif opcion == "4":
            print("Función: Devolver un libro.")

        elif opcion == "5":
            print("\n--- Libros Disponibles ---")
            libros_disponibles = biblioteca.mostrar_libros_disponibles()
            if libros_disponibles:
                for libro in libros_disponibles:
                    print(libro)  
            else:
                print("No hay libros disponibles.")

        elif opcion == "6":
            print("\n--- Usuarios Registrados ---")
            usuarios = biblioteca.mostrar_usuarios()
            if usuarios:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("No hay usuarios registrados.")
                
        elif opcion == "7":
            biblioteca.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

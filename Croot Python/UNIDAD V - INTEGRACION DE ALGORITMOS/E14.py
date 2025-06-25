"""
    **Sistema para registrar préstamos de libros (con control de disponibilidad).**
"""
import os

libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "estado": True},
    {"titulo": "1984", "autor": "George Orwell", "estado": True},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "estado": False},
    {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "estado": True},
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "estado": True},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "estado": True},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "estado": False},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "estado": True},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "estado": True},
    {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "estado": True},
    {"titulo": "Los juegos del hambre", "autor": "Suzanne Collins", "estado": False},
    {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "estado": True},
    {"titulo": "El código Da Vinci", "autor": "Dan Brown", "estado": True},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "estado": True},
    {"titulo": "It", "autor": "Stephen King", "estado": True},
    {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "estado": False},
    {"titulo": "Drácula", "autor": "Bram Stoker", "estado": True},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "estado": True},
    {"titulo": "La Odisea", "autor": "Homero", "estado": True},
    {"titulo": "Hamlet", "autor": "William Shakespeare", "estado": True}
]

prestamos = [
    {"lector": "Ana Torres", "titulo": "Don Quijote de la Mancha"},
    {"lector": "Luis Ramos", "titulo": "Crónica de una muerte anunciada"},
    {"lector": "Sofía Martínez", "titulo": "Los juegos del hambre"},
    {"lector": "Carlos Peña", "titulo": "Ensayo sobre la ceguera"}
]

#FUNCION MOSTRAR LIBROS
def mostrarLibros():
    print("LIBROS")
    print("=" * 40)
    for libro in libros:
        print(f"Titulo: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        if libro['estado']:
            print("Estado: Disponible")
        else:
            print("Estado: Prestado")
        print("-" * 40)
    q = input("Presiones Enter para Salir: ")
    os.system("cls")
    return

#FUNCION MOSTRAR PRESTAMOS
def mostrarPrestamos():
    print("PRESTAMOS")
    print("=" * 40)
    for value in prestamos:
        print(f"Lector: {value['lector']}")
        print(f"Titulo: {value['titulo']}")
        print("-" * 40)
    q = input("Presiones Enter para Salir: ")
    os.system("cls")
    return

#REGISTRAR PRESTAMO
def registrarPrestamo():
    os.system("cls")
    print("=" * 40)
    print("REGISTRAR PRESTAMO")
    print("=" * 40)
    print()
    lector = input("Lector: ").capitalize()
    titulo = input("Titulo: ").lower()
    encontrado = False
    for libro in libros:
        if titulo == libro['titulo'].lower():
            encontrado = True
            if libro['estado'] == False:
                print("El libro esta ocupado por otro lector, lo sentimos.")
                print("=" * 40)
                q = input("Presione Enter para Salir: ")
                os.system("cls")
                return
            elif libro['estado'] == True:
                libro["estado"] = False
                prestamos.append(
                    {
                        "lector": lector,
                        "titulo": titulo.capitalize()
                    }
                )
                print(f"Libro Registrado como prestado a {lector}.")
                print("=" * 40)
                q = input("Presione Enter para Salir: ")
                os.system("cls")
                return
        
    if encontrado == False:
        print("Libro no registrado en la biblioteca.")
        print("=" * 40)
        q = input("Presiones Enter para Salir: ")
        os.system("cls")
        return
            
#DEVOLVER PRESTAMO
def devolverPrestamo():
    os.system('cls')
    print("=" * 40)
    print("DEVOLVER PRESTAMO")
    print("=" * 40)
    print()
    lector = input("Lector: ").lower()
    titulo = input("Titulo: ").lower()
    bandera = False
    for prestamo in prestamos:
        if prestamo['lector'].lower() == lector and prestamo['titulo'].lower() == titulo:
            bandera = True
            prestamos.remove(prestamo)
            for estado in libros:
                if estado['titulo'].lower() == titulo:
                    estado['estado'] = True
                    break
            print("Libro devuelto.")
            print("=" * 40)
            q = input("Presiones Enter para Salir: ")
            os.system("cls")
            return
    if bandera == False:
        print(f"Prestamo no encontrado, para {lector.capitalize()} y el libro {titulo.capitalize()}")
        print("=" * 40)
        os.system("cls")
        return

#REGISTRAR NUEVO LIBRO
def registrarLibro():
    print("=" * 40)
    print("REGISTRAR NUEO LIBRO")
    print("=" * 40)
    print()
    titulo = input("Titulo: ").lower()
    autor = input("Autor: ").lower()
    bandera = False
    for libro in libros:
        if libro["titulo"].lower() == titulo and libro['autor'].lower() == autor:
            bandera = True
            print("Este libro ya se encuentra registrado.")
            print("=" * 40)
            q = input("Presiones Enter para Salir: ")
            os.system("cls")
            return
    if bandera == False:
        libros.append(
            {
                "titulo": titulo.capitalize(),
                "autor": autor.capitalize(),
                "estado": True   
            }
        )
        print("Libro Registrado con exito.")
        print("=" * 40)
        q = input("Presione Enter para Salir: ")
        os.system("cls")
        return

def quitarLibro():
    print("=" * 40)
    print("RETIRAR LIBRO DE LA BIBLIOTECA")
    print("=" * 40)
    print()
    titulo = input("Titulo: ").lower()
    autor = input("Autor: ").lower()
    encontrado = False
    for libro in libros:
        if titulo == libro['titulo'].lower() and autor == libro['autor'].lower():
            encontrado = True
            libros.remove(libro)
            print("Libro removido con exito.")
            print("=" * 40)
            q = input("Presiones Enter para Salir: ")
            os.system("cls")
            return
    if encontrado == False:
        q = input("Presione Enter para Salir: ")
        os.system("cls")
        return


#MENU
def main():
    os.system("cls")
    while True:
        print("SISTEMA DE PRESTAMOS")
        print("=" * 40)
        print("1) Mostrar Libros")
        print("2) Mostrar Prestamos")
        print("3) Registrar Prestamo")
        print("4) Devolver Libro")
        print("5) Registrar Libro Nuevo")
        print("6) Quitar Libro de la Biblioteca")
        print()
        print("0) Presione enter para salir.")
        print("-" * 40)
        option = int(input(" -> "))
        if option == 1:
            os.system("cls")
            mostrarLibros()
        elif option == 2:
            os.system("cls")
            mostrarPrestamos()
        elif option == 3:
            os.system("cls")
            registrarPrestamo()
        elif option == 4:
            os.system("cls")
            devolverPrestamo()
        elif option == 5:
            os.system("cls")
            registrarLibro()
        elif option == 6:
            os.system("cls")
            quitarLibro()
        elif option == 0:
            break

main()
"""
    **Mini agenda de contactos (con búsqueda por nombre).**
"""

import os
import re
contactos = [
    {"nombre": "Cleber Motte", "telefono": "901623995", "email": "cleber@example.com"},
    {"nombre": "Ana Torres", "telefono": "987654321", "email": "ana.torres@gmail.com"},
    {"nombre": "Luis Ramos", "telefono": "912345678", "email": "luis.ramos@yahoo.com"},
    {"nombre": "Sofía Martínez", "telefono": "956789123", "email": "sofia.mtz@outlook.com"},
    {"nombre": "Carlos Peña", "telefono": "983214567", "email": "carlos.pena@correo.com"},
    {"nombre": "Julia Mendoza", "telefono": "974563218", "email": "j.mendoza@empresa.pe"},
    {"nombre": "Mario Quispe", "telefono": "989812345", "email": "mario.q@correo.pe"},
    {"nombre": "Lucía Vargas", "telefono": "965432178", "email": "lucia.v@dominio.com"},
    {"nombre": "Andrés López", "telefono": "998877665", "email": "andres.lopez@correo.org"},
    {"nombre": "Valeria Huamán", "telefono": "911223344", "email": "valeria.huaman@hotmail.com"},
    {"nombre": "Esteban Ríos", "telefono": "934561289", "email": "esteban.rios@edu.pe"}
]


def mostrarcontactos():
    os.system("cls")
    print("=" * 15,"CONTACTOS","=" * 15)
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}")
        print(f"Numero: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")
        print("-" * 40)
    input("Volver atras... (Enter) ")
    return

def buscarxnombre():

    

    while True:
        os.system("cls")
        print("=" * 7,"BUSCAR CONTACTO POR NOMBRE","=" * 7)
        print()
        print("Regresar atras... (Enter)")
        buscar = input("Nombre: ").lower()
        if buscar == "":
            return
        encontrado = False
        for contacto in contactos:
            if contacto['nombre'].lower() == buscar:
                encontrado = True
                print()
                print("-" * 10,"CONTACTO ENCONTRADO:", "-" * 10)
                print(f"Nombre: {contacto['nombre']}")
                print(f"Numero: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print("-" * 40)
                continue
        
        if encontrado == False:
            print(f"No hemos encontrado a {buscar.capitalize()}.")
            print()
        input()

def buscarxnumero():
        
    while True:
        os.system("cls")
        print("=" * 7,"BUSCAR CONTACTO POR NUMERO","=" * 7)
        print()
        print("Regresar atras... (Enter)")
        buscar = input("Telefono: ")
        if buscar == "":
            return
        if buscar.isdigit():
            if len(buscar) != 9:
                print("Por favor ingresa solo numeros de 9 digitos.")
                input()
                continue
        else:
            print("Telefono invalido, intenta de nuevo.")
            input()
            continue

        encontrado = False
        for contacto in contactos:
            if contacto['telefono'] == buscar:
                encontrado = True
                print()
                print("=" * 10,"TELEFONO ENCONTRADO","=" * 10)
                print(f"Nombre: {contacto['nombre']}")
                print(f"Telefono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                print("-" * 40)
                continue
        if encontrado == False:
            print(f"No hemos encontrado el telefono {buscar}.")
            print()
        input()

def agregarcontacto():
        
    while True:
        os.system("cls")
        print("=" * 9,"AGREGAR NUEVO CONTACTO","=" * 9)
        print()
        nombre = input("Nombre: ").capitalize()
        existe = False
        while True:
            telefono = input("Telefono: ")
            if not telefono.isdigit():
                print("Telefono no valido, solo numeros por favor.")
                input()
                continue
            if telefono.isdigit():
                if len(telefono) != 9:
                    print("Telefono con rango incorrecto")
                    input()
                    continue
            for contacto in contactos:
                if contacto['telefono'] == telefono:
                    existe = True
                    print("El telefono ya esta registrado, no puedes crear nuevo contacto.")
                    break
                    
            if telefono.isdigit():
                if len(telefono) == 9:
                    break
        if existe == True:
            input()
            return
        
        while True:
            patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            email = input("Email: ")
            if not re.match(patron, email):
                print("correo no valido, intente de nuevo")
                input()
            if re.match(patron, email):
                break
        contactos.append(
            {
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }
        )
        print()
        print("AGREGADO CORRECTAMENTE.")
        input()
        break
    return

def eliminarcontacto():
    
    while True:
        os.system("cls")
        print("=" * 11,"ELIMINAR CONTACTO","=" * 11)
        print()
        while True:
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            if nombre == "" or telefono == "":
                return
            encontrado = False
            for contacto in contactos:
                if contacto['nombre'].lower() == nombre.lower() and contacto["telefono"] == telefono:
                    encontrado = True
                    print()
                    print("-" * 40)
                    print(f"Nombre: {contacto['nombre']}")
                    print(f"Telefono: {contacto['telefono']}")
                    print(f"Email: {contacto['email']}")
                    print("-" * 40)
                    print("Estas seguro de eliminar?")
                    confirmacion = input("s/n: ").lower()
                    if confirmacion == "s":
                        contactos.remove(contacto)
                        print("Eliminacion completada.")
                        input()
                        return
                    else:
                        return
            if encontrado == False:
                print("Contacto no encontrado.")
                input()

    
def main():
    while True:
        os.system("cls")
        print("=" * 10,"AGENDA DE CONTACTOS","=" * 10)
        print(r"""
         /\_/\ 
        ( •ᴥ• )
         > ^ <
        """)
        print("-" * 40)
        print()
        print("1) MOSTRAR CONTACTOS")
        print("2) BUSCAR CONTACTO POR NOMBRE")
        print("3) BUSCAR CONTACTO POR NUMERO")
        print("4) AGREGAR CONTACTO NUEVO")
        print("5) ELIMINAR CONTACTO")
        print()
        print("-" * 40)
        print("Digite su opcion o presione Enter para salir.")
        op = input("-> ")
        if not op.isdigit():
            break
        option = int(op)
        if option == 1:
            mostrarcontactos()
        elif option == 2:
            buscarxnombre()
        elif option == 3:
            buscarxnumero()
        elif option == 4:
            agregarcontacto()
        elif option == 5:
            eliminarcontacto()
        else:
            print("opcion no valida, ingresa de nuevo.")
            input("Enter para continuar...")
main()

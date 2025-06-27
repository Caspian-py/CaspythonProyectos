"""
2. Simulador de ventas y stock
•	Funcionalidades: catálogo, carrito, pago simulado, control de inventario
•	Estructura: diccionarios para representar productos y stock.
•	Aprendes: lógica secuencial compleja y estructuras anidadas.

"""
import json
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ImportarJson():
    try:
        with open("catalogo.json", "r") as f:
            catalogo = json.load(f)
            return catalogo
    except FileNotFoundError:
        print("Archivo Json no encontrado en la carpeta.")

catalogo = ImportarJson()

def ImportarJsonUsser():
    try:
        with open("adm.json", "r") as f:
            adm = json.load(f)
            return adm
    except FileNotFoundError:
        return [{"usuario": "caspian", "codigo": 12345}]
    
adm = ImportarJsonUsser()
    


def Guardarjson(catalogo):
    with open("catalogo.json", "w") as f:
        json.dump(catalogo, f, indent=4)


def MostrarCatalogoMenu():
    print("CATALOGO:")
    print("-" * 40)
    for id, producto in enumerate(catalogo):
        if producto['stock'] > 0:
            print(f"ID: {id + 1}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Stock: {producto['stock']}")
            print("-" * 40)

def MostrarCatalogoAdm():
    print("LOGIN")
    usser = input("Usuario: ").strip().lower()
    password = int(input("Contraseña: "))
    if any(usser == u['usuario'] and password == u['clave'] for u in adm):
        print(f"BIENVENIDO {usser.upper()}")
        print()
        print("CATALOGO COMPLETO")
        try:
            print("-" * 40)
            for id, producto in enumerate(catalogo):
                print(f"ID: {id + 1}")
                print(f"Nombre: {producto['nombre']}")
                print(f"Stock: {producto['stock']}")
                print("-" * 40)
        except TypeError:
            print("Catalogo Vacio.")
    else:
        print("CREDENCIALES INVALIDAS.")







clear()

MostrarCatalogoAdm()


Guardarjson(catalogo)



"""
2. Simulador de ventas y stock
•	Funcionalidades: catálogo, carrito, pago simulado, control de inventario
•	Estructura: diccionarios para representar productos y stock.
•	Aprendes: lógica secuencial compleja y estructuras anidadas.

"""
import json
import os
ancho = os.get_terminal_size().columns
import getpass

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ImportarJson():
    try:
        with open("catalogo.json", "r") as f:
            catalogo = json.load(f)
            return catalogo
    except FileNotFoundError:
        return []
        

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

def Login():
    clear()
    print("🔐 LOGIN 🔐".center(ancho))
    print()
    try:
        print("USUARIO 👤: ")
        usuario = input(">> ").lower().strip()
        print("CONTRASEÑA 🔑: ")
        password = int(getpass.getpass(">> "))
    except ValueError:
        input("CREDENCIALES INVALIDAS ❌⚠️ ")
        return False
    if any(usuario == u['usuario'] and password == u['clave'] for u in adm):
        return True
    else:
        input("CREDENCIALES INVALIDAS ❌⚠️ ")
        return False

def MostrarCatalogoMenu():
    print("📦 CATALOGO DISPONIBLE 📦".center(ancho))
    print("-" * 50)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Stock':^5}")
    print("-" * 50)
    
    for id, producto in enumerate(catalogo):
        if producto['stock'] > 0:
            print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['stock']:^5} U")
    if len(catalogo) <= 0:
        print("❌ CATALOGO VACIO ❌".center(25))
    print("-" * 50)

def MostrarCatalogoAdm():
    
    print("📦 CATALOGO COMPLETO 📦".center(ancho))
    print("-" * 50)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Stock':^5}")
    print("-" * 50)
    
    for id, producto in enumerate(catalogo):
        print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['stock']:^5} U")
    if len(catalogo) <= 0:
        print("❌ CATALOGO VACIO ❌".center(25))
    print("-" * 50)

def agregar():
    while True:
        clear()
        print("AGREGAR PRODUCTO NUEVO".center(ancho))
        print()
        MostrarCatalogoAdm()
        print("NUEVO PRODUCTO: ")
        print()
        nombre = input("Nombre Producto: ").strip().lower()
        stock = int(input("Stock: "))
        if any(nombre == p['nombre'].lower() for p in catalogo):
            input("NOMBRE DE PRODUCTO YA ESTA AGREGADO")
            continue
        input()
    
        


def MenuAdministrador():
    if not Login():
        print("CREDENCIALES INVALIDAS ❌⚠️")
    else:
        while True:
            clear()
            print("✅ BIENVENIDO AL ENTORNO ADMIN ✅".center(ancho))
            print()
            MostrarCatalogoAdm()
            print("📋 MENU OPCIONES: ")
            print()
            print("➕ AGREGAR: ")
            print("✏️  MODIFICAR")
            print("🗑️  ELIMINAR")
            print("🔒 CERRAR SESION")
            print()
            opt = input("🔎 OPCION: ").strip().lower()

            if opt in ("salir", "cerrar", "cerrar sesion"):
                return
            elif opt == "agregar":
                agregar()
            elif opt == "modificar":
                input("LLAMAMOS A LA FUNCION MODIFICAR")
            elif opt == "eliminar":
                input("LLAMAMOS A LA FUNCION ELIMINAR")
            else:
                input("OPCION NO ENCONTRADA EN EL MENU ❌⚠️ ")

def main():
    while True:
        clear()
        print("🛍️ SIMULADOR DE VENTAS - CASPIAN 🛍️".center(ancho))
        print()
        MostrarCatalogoMenu()
        print("📋 MENU OPCION:")
        print()
        print("🧾 CAJA")
        print("🛒 MODIFICAR CARRITO")
        print("🔐 INICIAR SESION")
        print("❌ SALIR")
        print()
        opt = input("🔎 ID u OPCION: ").strip().lower()

        if not opt.isdigit():
            if opt == "salir":
                break
            elif opt in ("caja", "pagar"):
                input("Llevamos al usuario a la caja.")
            elif opt in ("modificar", "modificar carrito"):
                input("Llevamos al usuario al menu de modificar carrito.")
            elif opt in ("iniciar sesion", "iniciar"):
                MenuAdministrador()
            else:
                input("OPCION NO ENCONTRADA EN EL MENU. ❌⚠️ ")
            
        elif opt.isdigit():
            input("Selecciona en el carrito")


main()
        





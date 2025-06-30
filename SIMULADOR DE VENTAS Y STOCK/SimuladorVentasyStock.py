"""
2. Simulador de ventas y stock
•	Funcionalidades: catálogo, carrito, pago simulado, control de inventario
•	Estructura: diccionarios para representar productos y stock.
•	Aprendes: lógica secuencial compleja y estructuras anidadas.

"""
import json
import os
import random
ancho = os.get_terminal_size().columns
import getpass
import string

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
carro = []
def ImportarJsonUsser():
    try:
        with open("adm.json", "r") as f:
            adm = json.load(f)
            return adm
    except FileNotFoundError:
        return [{"usuario": "caspian", "codigo": 12345}]
    
adm = ImportarJsonUsser()
    


def Guardarjson(catalogo):
    try:
        with open("catalogo.json", "w") as f:
            json.dump(catalogo, f, indent=4)
            return True
    except (PermissionError, OSError):
        return False

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
    print("-" * 60)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Precio':<10} | {'Stock':^5}")
    print("-" * 60)
    
    for id, producto in enumerate(catalogo):
        if producto['stock'] > 0:
            print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['precio']:<10} | {producto['stock']:^5} U")
    if len(catalogo) <= 0:
        print("❌ CATALOGO VACIO ❌".center(30))
    print("-" * 60)

def MostrarCatalogoAdm():
    
    print("📦 CATALOGO COMPLETO 📦".center(ancho))
    print("-" * 60)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Precio':<10} | {'Stock':^5}")
    print("-" * 60)
    
    for id, producto in enumerate(catalogo):
        print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['precio']:<10} | {producto['stock']:^5} U")
    if len(catalogo) <= 0:
        print("❌ CATALOGO VACIO ❌".center(30))
    print("-" * 60)

def agregar():
    while True:
        clear()
        print("🆕 AGREGAR PRODUCTO NUEVO 🆕".center(ancho))
        print()
        print("NUEVO PRODUCTO 📦: ")
        print()
        nombre = input("🏷️  Nombre Producto: ").strip().lower()
        if len(nombre) < 4:
            input("NOMBRE DEMASIADO CORTO ❌⚠️")
            continue
        elif nombre.lower() == "cancelar":
            return
        try:
            precio = float(input("Precio 💰: "))
            if precio <= 0:
                raise ValueError
        except ValueError:
            input("PRECIO INVALIDO ❌⚠️")
            continue
        try:
            stock = int(input("Stock 🔢: "))
            if stock < 0:
                raise ValueError
        except ValueError:
            input("STOCK INVALIDO ❌⚠️")
            continue
        
        if any(nombre == p['nombre'].lower() for p in catalogo):
            input("EL PRODUCTO YA ESTA REGISTRADO ❌⚠️")
            continue
        else:
            catalogo.append(
                {
                    "nombre": nombre.capitalize(),
                    "precio": round(precio, 2),
                    "stock": stock
                }
            )
            if Guardarjson(catalogo):
                input("AGREGADO CORRECTAMENTE ✅")
            else:
                input("ERROR AL AGREGAR EL PROPUCTO ❌⚠️")
        if input("➕ DESEAR AGREGAR OTRO? S/N: ").strip().lower() != "s":
            return  
              
def modificar():
    while True:
        clear()
        print("✏️ MODIFICAR PRODUCTO ✏️".center(ancho))
        print()
        MostrarCatalogoAdm()
        print("🔢 SELECCIONA EL ID (0 para salir):")
        try:
            idi = int(input("ID 🔢: "))
            if idi == 0:
                return
            id = idi - 1
        except ValueError:
            input("ID NO VALIDO ❌⚠️")
            continue
        if id >= len(catalogo) or id < 0:
            input("ID NO ENCONTRADO ❌⚠️")
            continue
        else:
            
            while True:
                clear()
                print("🔧 MODIFICANDO PRODUCTO...")
                print(f"{'Nombre':<20} | {'Precio':<10} | {'Stock':^5}")
                print("-" * 45)
                print(f"{catalogo[id]['nombre']:<20} | {catalogo[id]['precio']:<10} | {catalogo[id]['stock']:^5} U")
                print("-" * 45)
                n = input("🏷️  Nombre Nuevo: ").strip().lower()
                if n == "cancelar":
                    break
                elif len(n) < 4:
                    input("NOMBRE DEMASIADO CORTO ❌⚠️")
                    continue
                if n != catalogo[id]['nombre'].lower().strip():
                    if any(n == p['nombre'].lower().strip() for p in catalogo):
                        input("NOMBRE YA REGISTRADO ❌⚠️")
                        continue
                try:
                    p = float(input("Precio 💰: "))
                    if p <= 0:
                        raise ValueError
                except ValueError:
                    input("PRECIO INVALIDO ❌⚠️")
                    continue
                try:
                    s = int(input("📦 Stock Nuevo: "))
                    if s < 0:
                        raise ValueError
                except ValueError:
                    input("STOCK INVALIDO ❌⚠️")
                    continue
                catalogo[id]['nombre'] = n.capitalize()
                catalogo[id]['precio'] = round(p, 2)
                catalogo[id]['stock'] = s
                break
            Guardarjson(catalogo)

        if input("DESEAR MODIFICAR OTRO PRODUCTO? (S/N) ➕: ").strip().lower() != "s":
            return
        
def eliminar():
    while True:
        clear()
        print("🗑️ ELIMINAR PRODUCTO 🗑️".center(ancho))
        MostrarCatalogoAdm()
        print("SELECCIONA EL ID (0 para salir) 🔢")
        
        try:
            idi = int(input("ID 🔢: "))
            if idi == 0:
                return
            id = idi - 1
            if id < 0 or id >= len(catalogo):
                raise ValueError
        except ValueError:
            input("ID NO VALIDO")
            continue
        clear()
        print("🗑️ ELIMINANDO PRODUCTO...")
        print(f"{'Nombre':<20} | {'Precio':<10} | {'stock':^5}")
        print("-" * 45)
        print(f"{catalogo[id]['nombre']:<20} | {catalogo[id]['precio']:<10} | {catalogo[id]['stock']}")
        print("-" * 45)
        codigo = ''.join(random.choices(string.ascii_letters + string.digits, k = 5))
        print(f"CODIGO DE CONFIRMACION 🔐: {codigo}")
        if input("INGRESA EL CODIGO EXACTAMENTE PARA CONFIRMAR ELIMINACION ✏️🔐: ") == codigo:
            catalogo.pop(id)
            Guardarjson(catalogo)
            print("PRODUCTO ELIMINADO CORRECTAMENTE ✅")
        else:
            print("ELIMINACION CANCELADA 🚫")
        if input("DESEAR ELIMINAR OTRO PRODUCTO? (S/N) ➕: ").lower().strip() != "s":
            return

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
                modificar()
            elif opt == "eliminar":
                eliminar()
            else:
                input("OPCION NO ENCONTRADA EN EL MENU ❌⚠️ ")
def MostrarCarro():
    print("CARRO DE COMPRAS".center(ancho))
    print("-" * 60)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Precio':<10} | {'Stock':^5}")
    print("-" * 60)

    if len(carro) <= 0:
        print("CARRO VACIO".center(60))
    else:
        for id, producto in enumerate(carro):
            print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['precio']:<10} | {producto['stock']:^5}")
    print("-" * 60)

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
        MostrarCarro()
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
            id = int(opt) - 1
            if id >= len(catalogo) or catalogo[id]['stock'] == 0 or id <= 0:
                input("ID NO VALIDO ❌⚠️")
            else:
                carro.append(catalogo[id])


main()
        





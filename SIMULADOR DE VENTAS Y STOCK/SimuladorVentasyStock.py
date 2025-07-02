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
    print("CARRO DE COMPRAS".center(60))
    print("-" * 60)
    print(f"{'ID':^4} | {'Nombre':<25} | {'Precio':<10} | {'Cantidad':^5}")
    print("-" * 60)

    if len(carro) <= 0:
        print("CARRO VACIO".center(60))
    else:
        for id, producto in enumerate(carro):
            print(f"{id + 1:^4} | {producto['nombre']:<25} | {producto['precio']:<10} | {producto['cantidad']:^5}")
    print("-" * 60)

def SeleccionProducto(id):
    while True:
        clear()
        print("PRODUCTO SELECCIONADO")
        print("-" * 40)
        print(f"{'Nombre':<20} | {'Precio':<10} | {'Stock':^5}")
        print("-" * 40)
        print(f"{catalogo[id]['nombre']:<20} | {catalogo[id]['precio']:<10} | {catalogo[id]['stock']:^5}")
        print("-" * 40)
        print()
        try:
            cantidad = int(input("Cantidad (0 para cancelar): "))
            if cantidad < 0:
                raise ValueError
            elif cantidad == 0:
                return
        except ValueError:
            input("CANTIDAD INVALIDA.")
            continue

        if cantidad > catalogo[id]['stock']:
            input("NO TENEMOS DISPONIBLE ESA CANTIDAD.")
            continue
        else:
            
            catalogo[id]['stock'] -= int(cantidad)

            if any(catalogo[id]['nombre'] == p['nombre'] for p in carro):
                for p in carro:
                    if p['nombre'] == catalogo[id]['nombre']:
                        p['cantidad'] += cantidad
                        p['precio'] = catalogo[id]['precio'] * p['cantidad']  
                        break
                input("Compra agregada a carrito")
                return
            else:
                carro.append(
                    {
                        "nombre": catalogo[id]['nombre'],
                        "precio": catalogo[id]['precio'] * cantidad,
                        "cantidad": cantidad
                    }
                )
                Guardarjson(catalogo)
                input("Compra agregada a carrito")
                return

def ModificarCarro(id):
    clear()
    print("MODIFICANDO CARRITO...")
    print("-" * 40)
    print(f"{'Nombre':<20} | {'Precio':<10} | {'Cantidad':^5}")
    print("-" * 40)
    print(f"{carro[id]['nombre']:<20} | {carro[id]['precio']:<10} | {carro[id]['cantidad']:^5}")
    print("-" * 40)
    print()
    for idc, producto in enumerate(catalogo):
        if producto['nombre'] == carro[id]['nombre']:
            idp = idc
            break
    try:
        cantidad = int(input("Cantidad (0 para eliminar y Enter cancelar): "))
        if cantidad == 0:
            catalogo[idp]['stock'] += carro[id]['cantidad']
            carro.pop(id)
            input("ELIMINADO")
            return
    except ValueError:
        input("modificacion cancelada.")
        return
    if cantidad < 0:
        input("CANTIDAD INVALIDA ❌⚠️")
        return
    
    if cantidad > catalogo[idp]['stock']:
        input("NO HAY SUFICIENTE STOCK")
        return
    else:
        carro[id]['cantidad'] += cantidad
        carro[id]['precio'] = carro[id]['precio'] * cantidad
        catalogo[idp]['stock'] -= cantidad
        input("modificado correctamente.")
    Guardarjson(catalogo)

def CancelarCompra():
    
    for p in carro:
        for pro in catalogo:
            if p['nombre'] == pro['nombre']:
                pro['stock'] += p['cantidad']
                break
    carro.clear()
    Guardarjson(catalogo)
    return

def MenuModificar():
    while True:
        clear()
        print("MODIFICAR CARRO")
        MostrarCarro()
        print()
        try:
            id = int(input("ID A MODIFICAR (0 para cancelar): "))
            if id < 0:
                raise ValueError
            elif id == 0:
                return
        except ValueError:
            input("ID NO VALIDP")
            continue
        id -= 1
        if id > len(carro):
            input("ID NO ENCONTRADO")
        else:
            ModificarCarro(id)

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
                CancelarCompra()
                break
            elif opt in ("caja", "pagar"):
                input("Llevamos al usuario a la caja.")
            elif opt in ("modificar", "modificar carrito"):
                if len(carro) == 0:
                    input("CARRO VACIO NO SE PUEDE MODIFICAR.")
                else:
                    MenuModificar()
            elif opt in ("iniciar sesion", "iniciar"):
                MenuAdministrador()
            else:
                input("OPCION NO ENCONTRADA EN EL MENU. ❌⚠️ ")
            
        elif opt.isdigit():
            id = int(opt) - 1
            
            if id >= len(catalogo) or catalogo[id]['stock'] == 0 or id < 0:
                input("ID NO VALIDO ❌⚠️")
                input(catalogo[id])
            else:
                SeleccionProducto(id)
                Guardarjson(catalogo)

main()
        

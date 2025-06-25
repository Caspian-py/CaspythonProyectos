"""
    **Gestión de inventario simple:**
    Leer una lista de productos con nombre, precio y stock.

    * Permitir al usuario hacer compras hasta que decida salir.
    * Restar del inventario y calcular total a pagar.
"""
import random
import os
inventario = []
def limpiar():
    os.system("cls")

for _ in range(random.randint(1,2)):
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))

    inventario.append(
        {
            "nombre": nombre,
            "precio": precio,
            "stock": stock
        }
    )
limpiar()

def mostrar():
    print("INVENTARIO DISPONIBLE")
    print("-" * 40)
    for values in inventario:
        print(f"Nombre: {values["nombre"].capitalize()}")
        print(f"Precio: {values["precio"]} soles")
        print(f"stock: {values["stock"]}")
        print("-" * 40)
    print("salir: Esribe salir.")
def comprar():
    totalPagar = 0
    while True:
        mostrar()
        comprar = input("\nQue vas a comprar?: ").lower()
        if comprar == "salir":
            break
        producto = None
        for item in inventario:
            if item["nombre"].lower() == comprar:
                producto = item
                break
        if producto is None:
            print("Producto no encontrado, intentelo nuevvamente.")
            continue
        cantidad = int(input(f"Cuantas unidades de {producto['nombre']} desea comprar?: "))
        if cantidad > producto['stock']:
            print(f"No hay suficiente Stock. Solo quedadn {producto['stock']} unidades.")
            continue
        producto['stock'] -= cantidad
        subtotal = cantidad * producto['precio']
        totalPagar += subtotal
        limpiar()
        print(f"Has comprado {cantidad} unidades de {producto['nombre']} por {subtotal:.2f}")
        print(f"\nTOTAL ACUMULADO: {totalPagar:.2f}")
    limpiar()
    print("\n----------Compra Finalizasa----------")
    print(f"Total a pagar: {totalPagar:.2f} soles")
    
comprar()

"""
    **Simulador de menú de cafetería (con acumulador de pedidos y total).**
"""
import os
import time
import random

menu = [
    {"codigo": 1, "nombre": "Café Americano", "precio": 5.00},
    {"codigo": 2, "nombre": "Café Espresso", "precio": 4.50},
    {"codigo": 3, "nombre": "Capuccino", "precio": 6.50},
    {"codigo": 4, "nombre": "Café Latte", "precio": 6.00},
    {"codigo": 5, "nombre": "Té de Hierbas", "precio": 4.00},
    {"codigo": 6, "nombre": "Brownie", "precio": 4.00},
    {"codigo": 7, "nombre": "Croissant", "precio": 3.50},
    {"codigo": 8, "nombre": "Muffin de Arándano", "precio": 4.50},
    {"codigo": 9, "nombre": "Galleta de Chocolate", "precio": 2.50},
    {"codigo": 10, "nombre": "Sandwich Mixto", "precio": 7.00}
]
carro = []

def boleta():
    os.system("cls")
    print()
    print("-" * 15,"CROOT PAY","-" * 15)
    print()
    print("Tus pedidos:")
    print("-" * 40)
    totalP = 0
    codigo = random.randint(10000,99999)
    for compra in carro:
        print(f" - {compra["cantidad"]} {compra["nombre"]} {compra["precio"]}")
        totalP += (compra["precio"] * compra["cantidad"])
    print("-" * 40)
    print(f"TOTAL: {totalP} soles.")
    print(f"CODIGO PAY: {codigo}")
    print("-" * 40)
    print()
    while True:
        print("PARA REALIZAR EL PAGO DIGITE EL CODIGO UNICO DE PAGO.")
        print("CANCELAR COMPRA (cancelar)")
        cod = input("COD: ")
        if cod.lower() == "cancelar":
            print("COMPRA CANCELADA, GRACIAS POR SU VISITA.")
            break
        else:

            if cod.isdigit():
                if len(cod) != 5 or cod != codigo:
                    print("Codigo Invalido.")
                if len(cod) == 5 and int(cod) == codigo:
                    os.system("cls")
                    print("=" * 14,"CROOT COOKIE", "=" * 14)
                    print()
                    print("SE HA REALIZADO LA TRANFERENCIA CORRECTAMENTE.")
                    print(f"{totalP} ✅")
                    print("GRACIAS POR SU COMPRA.")
                    print("🌟" * 40)
                    break
            else:
                print("Codigo Invalido.")



def main():
    while True:
        os.system("cls")
        print()
        print("=" * 14, "CROOT COOKIE", "=" * 14)
        print()
        print("-" * 17, "CARTA", "-" * 17)
        print()
        print("BEBIDAS:")
        print("-" * 40)
        for men in menu:
            if men["codigo"] < 6:
                print(f"COD: {men['codigo']}")
                print(f"Nombre: {men['nombre']}")
                print(f"Precio: {men['precio']}")
                print("-" * 40)
        print()
        print("COMIDAS/DULCES")
        print("-" * 40)
        for men in menu:
            if men["codigo"] > 5:
                print(f"COD: {men['codigo']}")
                print(f"Nombre: {men['nombre']}")
                print(f"Precio: {men['precio']}")
                print("-" * 40)
        print()
        
        print("=" * 16, "CARRITO", "=" * 16)
        total = 0
        for carrito in carro:
            print(f"{carrito["cantidad"]} {carrito["nombre"]} {carrito["precio"]}")
            total += (carrito["precio"] * carrito["cantidad"])
        print('-' * 40)
        print(f"TOTAL: {total}")
        print("=" * 40)
        salir = False
        pagar = False
        while True:
            
            print("SALIR: 2 veces (Enter)")
            print("PAGAR: 0 y 0")
            print()
            cantidad = input("Cantidad: ")
            select = input("Cod: ")
            if cantidad == "" and select == "":
                salir = True
                break
            elif int(cantidad) == 0 and int(select) == 0:
                pagar = True
                break
            if not cantidad.isdigit() or not select.isdigit():
                print("Por favor ingresa digitos.")
                input()
            else:
                break

        if salir == True:
            break
        if pagar == True:
            boleta()
            break

        existe = False
        
        for men in menu:
            if int(select) == men["codigo"]:
                existe = True
                repetida = False
                if len(carro) != 0:
                    for carrito in carro:
                        if carrito["nombre"] == men["nombre"]:
                            repetida = True
                            carrito['cantidad'] += int(cantidad)
                    if repetida == False:
                        carro.append({
                            "cantidad": int(cantidad),
                            "nombre": men["nombre"],
                            "precio": men["precio"]
                        })
                            
                elif len(carro) == 0:
                    carro.append({
                            "cantidad": int(cantidad),
                            "nombre": men["nombre"],
                            "precio": men["precio"]
                        })
                
        if existe == False:
            print("El codigo no existe.")
            input()
            continue

main()


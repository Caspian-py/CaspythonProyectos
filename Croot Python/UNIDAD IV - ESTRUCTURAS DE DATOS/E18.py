"""
    **Leer una lista de precios y aplicar un descuento del 10% a cada uno.**
"""

import random
precios = [
    {
        "nombre": (producto := input(f"Nombre del producto {id + 1}: ")),
        "precio": (precio := float(input(f"Precio del {producto}: "))),
        "descuento": round(precio * 0.9, 2)
    }
    for id in range(random.randint(5, 10))
]

print("\nResultado con decuento del 10%\n")
print("-" * 40)
for p in precios:
    print(f"Producto: {p["nombre"]}")
    print(f"Precio: {p["precio"]:.2f}")
    print(f"Descuento 10%: {p["descuento"]:.2f}")
    print("-" * 40)

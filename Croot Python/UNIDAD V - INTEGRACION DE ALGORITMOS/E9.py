"""
    **Concesionaria de autos:**
    Leer marca, modelo, precio de N autos.

    * Mostrar el más caro y el más barato.
    * Calcular el promedio de precios.
    * Mostrar todos los autos que valen menos del promedio.
"""
import random
autos = []

for id in range(random.randint(5, 10)):
    print(f"AUTO {id + 1}")
    print('-' * 40)
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = float(input("Precio: "))
    print("-" * 40)

    autos.append(
        {
            "marca": marca,
            "modelo": modelo,
            "precio": precio
        }
    )

def mostrar():
    print("-" * 40)
    for auto in autos:
        print(f"Marca: {auto['marca'].capitalize()}")
        print(f"Modelo: {auto['modelo'].capitalize()}")
        print(f"Precio: S/. {auto['precio']:.2f} soles.")
        print("-" * 40)
    
def caroybaroto():
    caro = max(autos, key=lambda a: a['precio'])
    print("CARRO MAS CARO:")
    print("-" * 40)
    print(f"Marca: {caro['marca']}")
    print(f"Modelo: {caro['modelo']}")
    print(f"Precio: {caro['precio']}")
    print("-" * 40)
    print()
    barato = min(autos, key=lambda a: a['precio'])
    print("CARRO MAS BARATO:")
    print("-" * 40)
    print(f"Marca: {barato['marca'].capitalize()}")
    print(f"Modelo: {barato['modelo'].capitalize()}")
    print(f"Precio: S/. {barato['precio']:.2f} soles")
    print("-" * 40)

def promedioymenos():
    suma = 0
    for auto in autos:
        suma += auto['precio']
    promedio = suma / len(autos)
    print(f"El promedio de precios es {promedio}")
    print()
    print("-" * 40)
    print("AUTOS QUE VALEN MENOS DEL PROMEDIO")
    print("-" * 40)
    for auto in autos:
        if auto['precio'] < promedio:
            print(f"Marca: {auto['marca'].capitalize()}")
            print(f"Modelo: {auto['modelo'].capitalize()}")
            print(f"Precio: S/. {auto['precio']:.2f} soles.")
            print("-" * 40)

mostrar()
caroybaroto()
promedioymenos()
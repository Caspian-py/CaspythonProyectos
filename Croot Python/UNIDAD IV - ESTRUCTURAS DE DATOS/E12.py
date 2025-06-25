"""
    **Buscar un número en un vector y mostrar su posición (si existe).**
"""
import random
numeros = []
for values in range(random.randint(5, 20)):
    numeros.append(random.randint(0,100))
print(numeros)
print()
print("BUSCADOR")
while True:
    values = int(input("Buscar: "))
    if values in numeros:
        print(f"El numero existe en la posicion {numeros.index(values) + 1}.")
        break
    else:
        print("No encontrado.")

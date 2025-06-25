"""
    **Leer un vector y decir si un número buscado está presente.**
"""
import random
numeros = []

for id in range(10):
    value = random.randint(1, 20)
    numeros.append(value)

for value in numeros:
    print(value)
print()
print()

while True:
    num = int(input(f"Buscar: "))
    if num in numeros:
        print(f"Numero encontrado, en la posicion {numeros.index(num) + 1}")
        break
    else:
        print("Numero no encontrado.")
        
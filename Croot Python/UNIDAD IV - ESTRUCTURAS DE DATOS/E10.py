"""
    **Multiplicar todos los elementos de una matriz 3x3 por un escalar.**
"""
matriz = []
escalar = int(input("Ingrese el valor escalar: "))
for filas in range(3):
    fila = []
    print()
    print(f"Grupo ({filas + 1}): ")
    print()
    for columna in range(3):
        value = int(input(f"Valor ({columna + 1}): "))
        fila.append(value)
    matriz.append(fila)

print()
matrizEscalar = []
for value in matriz:
    print(value)
print()
for fila in matriz:
    filas = []
    for columna in fila:
        filas.append(columna * escalar)
    matrizEscalar.append(filas)

for values in matrizEscalar:
    print(values)



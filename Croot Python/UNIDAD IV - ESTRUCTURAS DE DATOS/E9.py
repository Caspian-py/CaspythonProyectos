"""
    **Sumar todos los elementos de una matriz 3x3.**
"""

matriz = []
for filas in range(3):
    fila = []
    print()
    print(f"Grupo ({filas + 1})... ")
    for columna in range(3):
        value = int(input(f"Valor ({columna + 1}):"))
        fila.append(value)
    matriz.append(fila)

print()
st = 0
for fila in matriz:
    print(fila)
    st += (sum(fila))

print(f"La suma de todos los elementos de la matriz 3x3 es: ({st}). ")
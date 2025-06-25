"""
    **Leer una matriz 4x4 y encontrar el mayor valor por columna.**
"""
numeros = [[float(input(f"Valor {id + 1}: ")) for id in range(4)] for id in range(4)]
print(numeros)
for columna in range(4):
    maximo = max(fila[columna] for fila in numeros)
    print(f"Mayor en la columna {columna}: {maximo}")
print("-" * 40)
for i, fila in enumerate(numeros):
    maximo = max(fila)
    print(f"Mayor en la fila {i}: {maximo}")



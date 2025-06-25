"""
    **Leer una matriz 3x3 y contar cuántos elementos están por encima del promedio total.**
"""

matriz = []
promedio = 0

for filas in range(3):
    columnas = []
    for columna in range(3):
        value = int(input(f"Valor ({columna + 1}): "))
        columnas.append(value)
    matriz.append(columnas)

print(matriz)
suma = 0
for lista in matriz:
    suma += sum(lista)
print(F"Suma: {suma}")
promedio = suma / (len(matriz[0]) + len(matriz[1]) + len(matriz[2]))

print(f"Promedio: {promedio}")
cont = 0
for filas in matriz:
    for columnas in filas:
        if columnas>promedio:
            cont += 1

print(f"Mayores del promedio: {cont}.")
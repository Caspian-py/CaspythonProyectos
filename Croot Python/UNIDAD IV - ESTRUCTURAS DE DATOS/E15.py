"""
    **Sumar dos matrices 3x3.**
"""
import random
m1 = []
m2 = []

for filas in range(3):
    columnas = []
    for columna in range(3):
        columnas.append(random.randint(0,100))
    m1.append(columnas)
for filas in range(3):
    columnas = []
    for columna in range(3):
        columnas.append(random.randint(0,100))
    m2.append(columnas)

print("Matriz 1")
print(m1)
print("Matriz 2")
print(m2)


m3 = [[m1[fila][columna] + m2[fila][columna] for columna in range(3)] for fila in range(3)]

print("Suma Matriz 1 y Matriz 2")
print(m3)


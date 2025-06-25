"""
    **Multiplicar dos matrices 2x2.**
"""
import random


m1 = [[random.randint(0, 100) for columna in range(2)] for fila in range(2)]
print(m1)
m2 = [[random.randint(0, 100) for columna in range(2)] for fila in range(2)]
print(m2)
m3 = [[m1[fila][columna] * m2[fila][columna] for columna in range(2)] for fila in range(2)]
print(m3)


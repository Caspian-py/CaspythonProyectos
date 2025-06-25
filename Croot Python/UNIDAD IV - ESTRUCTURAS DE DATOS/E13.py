"""
    Calcular el promedio por fila de una matriz 4x4.
 """


import random
m = [[random.randint(1,20) for id in range(4)] for id in range(4)]
print("MATRIZ 4X4")
for fila in m:
    print(f"{fila}")
print()
print("PROMEDIO FILAS")
print("*" * 40)
for id, fila in enumerate(m):
    print(f"Promedio Fila {id + 1}: {(sum(fila)/len(fila)):.2f}")
    print("-" * 40)

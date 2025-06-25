"""
    **Intercambiar los elementos de una fila con una columna en una matriz 3x3.**
"""
import random
m = [
    [random.randint(0, 10) for id in range(3)]
    for id in range(3)
]
print("Matriz original")
for value in m:
    print(value)
filaid = int(input("Fila (0 - 2): "))
columnaid = int(input("Columna (0 - 2) "))

ft = m[filaid][:]
m[filaid] = [m[id][columnaid] for id in range(3)]

for id in range(3):
    m[id][columnaid] = ft[id]

for value in m:
    print(value)


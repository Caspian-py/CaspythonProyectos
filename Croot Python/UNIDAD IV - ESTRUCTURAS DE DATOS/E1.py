"""
**Leer 10 números y mostrarlos en el orden en que se ingresaron.**
"""

mat = []
for id in range(10):
    value = float(input(f"Numero ({id + 1}): "))
    mat.append(value)
print("============================================")
for value in mat:
    print(value)
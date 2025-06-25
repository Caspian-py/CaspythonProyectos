"""
    **Leer 10 números y mostrarlos en orden inverso.**
"""
mat = []
for id in range(10):
    value = float(input(f"Numero ({id + 1}): "))
    mat.append(value)

matInv = mat[::-1]
for value in matInv:
    print(value, end=" ")

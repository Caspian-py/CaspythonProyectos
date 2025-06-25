"""
    **Leer un vector de 10 elementos y encontrar el mayor y el menor.**
"""
numeros = []
for id in range(10):
    numero = float(input(f"Numero ({id + 1}): "))
    numeros.append(numero)

print()
print(f"El numeros mayor del vector es {max(numeros)}.")
print(f"El numero menor del vector es {min(numeros)}.")
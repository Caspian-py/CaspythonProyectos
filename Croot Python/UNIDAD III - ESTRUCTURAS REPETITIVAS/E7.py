"""
    **Leer N calificaciones y obtener su promedio.**
"""

cantN = int(input("Cantidad de notas: "))
sumaN = 0
for i in range(cantN):
    nota = int(input(f"Nota ({i+1}): "))
    sumaN = sumaN + nota

promedio = sumaN / cantN
print()
print(f"El promedio es {promedio}.")

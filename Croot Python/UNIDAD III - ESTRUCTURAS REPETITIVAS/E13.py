"""
    **Leer una secuencia de temperaturas y calcular la media.**
"""

cantidad = int(input("Cuantas temperaturas ingresaras: "))
sumaT = 0
for id in range(cantidad):
    temp = float(input(f"Temperatura ({id + 1}): "))
    sumaT += temp
media = sumaT / cantidad
print(f"La media de las temperaturas es {media}.")


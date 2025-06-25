"""
    **Mostrar la suma de los cuadrados de los N prmeros números Ingresados.**
"""

n = int(input("Cantidad de numeros: "))
sc = 0
for id in range(n):
    num = float(input(f"Numero ({id + 1})"))
    sc += (num**2)

print(f"La suma es: {sc}")

"""
    **Promedio ponderado de 3 exámenes (25%, 25%, 50%)**
"""

print("PROMEDIO PONDERADO")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

pp = (n1 * 0.25) + (n2 * 0.25) + (n3 * 0.50)

print(f"Si tus notas son {n1}, {n2}, {n3} tu nota Poonderado es {pp}.")

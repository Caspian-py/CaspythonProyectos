"""
    **Obtener la suma de los primeros N números enteros.**
"""

hasta = int(input("Hasta que numero sumamos: "))
s = 0
for i in range(hasta):
    s = s + (i+1)

print(f"La suma es: {s}.")


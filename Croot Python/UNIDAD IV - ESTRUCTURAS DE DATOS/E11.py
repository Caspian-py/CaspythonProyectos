"""
    **Leer 10 nombres y mostrarlos alfabéticamente.**
"""

nombres = []
for id in range(10):
    nombre = input(f"Nombre ({id + 1}): ")
    nombres.append(nombre)

print()

nombres.sort(key=str.lower)

for values in nombres:
    print(f"{values.capitalize()}", end=" ")
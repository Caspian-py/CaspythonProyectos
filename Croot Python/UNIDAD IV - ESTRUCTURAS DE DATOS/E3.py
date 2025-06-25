"""
    **Leer 10 números y calcular su promedio.**
"""
snum = 0
for id in range(10):
    numero = float(input(f"Numero({id + 1}): "))
    snum += numero

promedio = snum / 10
print()
print(f"Promedio: {promedio}.")

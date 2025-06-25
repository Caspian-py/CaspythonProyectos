"""
    **Leer un vector de 10 elementos y contar cuántos son positivos, negativos y ceros.**
"""

negativos = 0
positivos = 0
ceros = 0
elementos = []
for id in range(10):
    value = float(input(f"Numero ({id + 1}): "))
    elementos.append(value)

for value in elementos:
    if value > 0:
        positivos += 1
    elif value < 0:
        negativos += 1
    elif value == 0:
        ceros += 1

print()
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")
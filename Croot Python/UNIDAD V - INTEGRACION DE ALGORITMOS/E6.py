"""
    **Estadísticas de clima semanal:**
    Leer temperaturas de 7 días.

    * Mostrar la más alta, la más baja, y la temperatura media.
    * ¿Cuántos días fueron calurosos (>25°C)?
"""
import os
temperaturas = []
for dia in range(7):
    temperatura = float(input(f"Dia {dia + 1} temperatura °C: "))
    temperaturas.append(temperatura)
os.system("cls")

for id in range(7):
    print(f"Dia {id + 1}: {temperaturas[id]}°C")

print(f"Temperatura maxima: {max(temperaturas)}°C ")
print(f"Temperatura minima: {min(temperaturas)}°C")
print(f"Temperatira Media: {sum(temperaturas)/len(temperaturas)}°C")
calurosos = 0
for temp in temperaturas:
    if temp>25:
        calurosos += 1
print(f"Dias calurosos (>25°C): {calurosos} dias.")



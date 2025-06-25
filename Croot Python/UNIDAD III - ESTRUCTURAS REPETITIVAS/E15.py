"""
    **Simular una suma acumulativa de dinero ahorrado por semanas.**
"""

semanas = int(input("Cuantas Semanas Ahorraras: "))
ahorro = []
for id in range(semanas):
    semana = float(input(f"Semana ({id + 1}): "))
    ahorro.append(semana)

print()
for id, ahorros in enumerate(ahorro):
    print(f"Ahorro de la semana({id + 1}): {ahorros}")

print(f"Total ahorrado es: {sum(ahorro)}")

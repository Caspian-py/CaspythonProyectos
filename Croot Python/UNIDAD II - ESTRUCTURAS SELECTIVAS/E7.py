"""
    **Determinar si un año es bisiesto.**
    (Aplicar regla básica: divisible por 4, y no por 100 salvo que sí por 400).
"""

anio = int(input("Anio: "))

if anio % 4 != 0:
    print(f"{anio} no es bisiesto.")
elif anio % 100 != 0:
    print(F"{anio} es bisiesto.")
elif anio % 400 != 0:
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")
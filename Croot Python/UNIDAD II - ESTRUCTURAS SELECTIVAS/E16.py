"""
    **Verificar si un trabajador tiene derecho a bono:**
    Bono si trabajó más de 40 horas.
"""

nombre = str(input("Nombre del trabajador: "))
ht = int(input("Horas Trabajadas: "))

if ht >= 40:
    print(f"{nombre}, Si tiene derecho a bono.")
else:
    print(f"{nombre}, No tiene derecho a bono.")
"""
    **Determinar cuántos estudiantes aprobaron un curso (nota ≥ 70).**
"""

estudiantes = int(input("Cantidad de Estudiantes: "))
aprobados = 0
for id in range(estudiantes):
    nota = float(input(f"Estudiante ({id + 1}): "))
    if nota >= 70:
        aprobados += 1

print()
print(f"Abrobados: {aprobados}.")
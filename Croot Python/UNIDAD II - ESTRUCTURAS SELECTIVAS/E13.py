"""
    **Verificar si una nota corresponde a una calificación válida (0 a 100).**
"""

nota = int(input("Nota: "))

if nota >= 0 and nota <= 100:
    print(f"{nota} es una nota valida.")
else:
    print(f"{nota} no es una nota valida.")
    
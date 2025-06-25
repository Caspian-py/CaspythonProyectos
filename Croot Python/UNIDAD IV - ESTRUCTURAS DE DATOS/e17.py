"""
    **Leer los nombres de 5 estudiantes y sus calificaciones, luego calcular sus promedios.**
"""

import random
estudiantes = []

for _ in range(5):
    nombre = input("Nombre: ")
    notas = [float(input(f"Nota ({id + 1}): ")) for id in range(random.randint(3,7))]
    promedio = sum(notas) / len(notas)
    
    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    }
    estudiantes.append(estudiante)

print("\nEStudiantes\n")

for e in estudiantes:
    print(f"Nombre: {e["nombre"]}")
    print(f"Notas: {e["notas"]}")
    print(f"Promedio {e["promedio"]:.2f}")
    print("-" *30)

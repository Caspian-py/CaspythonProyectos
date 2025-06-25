"""
    **Sistema de calificaciones:**
    Leer nombres y tres notas por estudiante.

    * Calcular promedio.
    * Mostrar quiénes aprobaron (>= 70) y su rango: A, B, C, D, F.
"""
import os
estudiantes = []
for _ in range(3):
    nombre = input("Nombre: ")
    notas = [float(input(f"Nota {nota + 1}: ")) for nota in range(3)]
    promedio = sum(notas) / len(notas)
    if promedio >= 90:
        rango = "A"
    elif promedio >= 80:
        rango = "B"
    elif promedio >= 70:
        rango = "C"
    elif promedio >= 60:
        rango = "D"
    else:
        rango = "F" 
    estudiantes.append(
        {
            "nombre": nombre,
            "notas": notas,
            "promedio": promedio,
            "rango": rango
        }
    )
    print()
os.system("cls")
print("LISTA DE ESTUDIANTES")
print("-" * 40)
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre'].capitalize()}")
    print(f"Notas: {estudiante['notas']}")
    print(f"Promedio: {estudiante['promedio']:.2f}")
    print(f"Rango: {estudiante['rango']}")
    print("-" * 40)
print()
print("APROBADOS >=70")
print("-" * 40)
for estudiante in estudiantes:
    if estudiante["promedio"] >= 70:
        print(f"Nombre: {estudiante['nombre'].capitalize()}")
        print(f"Notas: {estudiante['notas']}")
        print(f"Promedio: {estudiante['promedio']:.2f} ✅")
        print(f"Rango: {estudiante['rango']}")
        print("-" * 40)
print()
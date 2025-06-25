"""
    **Control de asistencia de alumnos:**
    Leer nombres y registros de asistencia de N estudiantes durante 5 días. Mostrar:

    * Promedio de asistencia por alumno.
    * Quién tuvo asistencia perfecta.
"""
n = int(input("Cantidad de estudiantes: "))

estudiantes = []

for _ in range(n):
    nombre = input("Nombre del Estudiante: ")
    asistencias = []
    for dia in range(1, 6):
        while True:
            entrada = input(f"asistencia del {dia} (s/n): ").lower()
            if entrada in ("s", "n"):
                break
            else:
                print("Entrada Invalida use (s/n).")
        asistencias.append(entrada == "s")
    estudiantes.append({
        "nombre": nombre,
        "asistencias": asistencias
    })

print("\n Resultados \n")

for estudiante in estudiantes:
    print("-" * 40)
    promedio = (sum(estudiante["asistencias"]) / len(estudiante["asistencias"])) *100
    print(f"[{estudiante["nombre"]}: {promedio:.2f}% de asistencias.")
    if all(estudiante["asistencias"]):
        print("Asistencia perfecta. ✅")
    print("-" * 40)


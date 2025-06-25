"""
    **Evaluar si una persona puede acceder a una beca:**
    Requiere promedio mayor a 85 y no haber reprobado materias.
"""

nombre = str(input("Como te llamas?: "))
promedio = float(input("Cuanto fue tu promedio?: "))
materias = str(input("Tienes materias Reprobadas? (si/no): "))

if promedio >= 85 and materias == "no":
    print(f"Felicidades {nombre}!!, si puedes acceder a la beca. ")
else:
    print(f"{nombre}, no puedes acceder a la beca.")


"""
    **Clasificación de calificación**
    Si es mayor o igual a 70, es aprobatoria; si no, reprobatoria.
"""

calificacion = float(input("Calificacion: "))

if calificacion >= 70:
    print(f"Tu calificacion es {calificacion}, tu clasificacion es APROBATORIA.")
else:
    print(f"Tu calificacion es {calificacion}, tu clasificacion es REPROBATORIA.")

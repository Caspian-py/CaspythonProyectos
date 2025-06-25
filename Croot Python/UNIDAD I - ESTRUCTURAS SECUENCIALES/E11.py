"""
    **Ahorro anual si se guarda el 15% del sueldo semanal**
    Entrada: sueldo semanal. Considerar 4 semanas al mes.
"""

print("ESTE ES TU AHORRO ANUAL.")
ss = float(input("Cuanto es tu sueldo semanal?: "))

st = 12 * 4
ahs = ss * 0.15
aa = ahs * st

print(f"Estimado usuario, cada semana tu ahorras {ahs} soles, en un anio de ahorro tendrias {aa} soles.")
 
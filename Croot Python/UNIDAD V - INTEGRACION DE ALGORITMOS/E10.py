"""
    **Control de producción de fábrica:**
        Para 10 empleados, leer la cantidad de piezas producidas en una semana.

        * Calcular bono si supera 100 piezas.
        * Total producido y quién fue el más eficiente.
"""
import os
empleados = []

for _ in range(5):
    nombre = input("Nombre: ").capitalize()
    piezasp = int(input("Piezas Producidas(1 semana): "))
    if piezasp > 100:
        bono = (piezasp - 100) * 1
        empleados.append(
            {
                "nombre": nombre,
                "piezasp": piezasp,
                "bono": bono
            }
        )
    else:
        empleados.append(
            {
                "nombre": nombre,
                "piezasp": piezasp,
            }
        )
os.system('cls')
print("LISTA DE EMPLEADOS")
print("-" * 40)
for empleado in empleados:
    if 'bono' in empleado:
        print(f"Nombre: {empleado['nombre']}")
        print(f"Piezas Producidas: {empleado['piezasp']}")
        print(f"Bono: {empleado['bono']} soles.")
    else:
        print(f"Nombre: {empleado['nombre']}")
        print(f"Piezas Producidas: {empleado['piezasp']}")
    print("-" * 40)
    
print()
total = sum(empleado['piezasp'] for empleado in empleados)
print(f"TOTAL PIEZAS PRODUCIDAS: {total} piezas.")
print("-" * 40)
MasEficiente = max(empleados, key=lambda e: e['piezasp'])
print("EL TRABAJADOR MAS EFICIENTE")
print("-" * 40)
print(f"Nombre: {MasEficiente['nombre']}")
print(f"Piezas Producidas: {MasEficiente['piezasp']}")
if 'bono' in MasEficiente:
    print(f"Bono: {MasEficiente['bono']} soles.")
print("-" * 40)

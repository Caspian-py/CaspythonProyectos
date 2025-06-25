"""
    **Simulador de nómina semanal:** 
    Para N trabajadores:

    * Leer nombre, horas trabajadas y pago por hora.
    * Calcular sueldo bruto.
    * Aplicar un descuento de 10% si gana más de 2000.
    * Mostrar el sueldo neto de todos.
"""

n = int(input("Numeros de empleados: "))

trabajadores = []

for _ in range(n):
    nombre = input("Nombre: ")
    horas = int(input("Horas Trabajadas: "))
    pagoH = float(input("Pago por Hora: "))
    bruto = horas * pagoH
    if bruto > 2000:
        neto = bruto * 0.90
    else:
        neto = bruto
    trabajadores.append(
        {
            "nombre": nombre,
            "horas": horas,
            "pago": pagoH,
            "bruto": bruto,
            "neto": neto
        }
    )

print("\nResumen de Nomina\n")
print("-" * 40)
for trabajador in trabajadores:
    print(f"Nombre: {trabajador["nombre"]}")
    print(f"horas: {trabajador["horas"]} horas.")
    print(f"Pago por Horas: {trabajador["pago"]} soles.")
    print(f"Sueldo Bruto: {trabajador["bruto"]} soles.")
    print(f"Sueldo Neto: {trabajador["neto"]} soles.")
print("*" * 40)
    


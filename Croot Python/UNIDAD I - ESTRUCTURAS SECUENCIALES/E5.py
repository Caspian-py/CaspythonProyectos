"""
    Presupuesto de pintura por m²:
    Calcula el costo total para pintar una superficie multiplicando el área en metros cuadrados por el costo
    fijo por m².
"""

print("HOLA USUARIO, VAMOS A CALCULAR CUANTO TENDRAS QUE PAGAR POR EL PINTADO.")

tm2 = float(input("Cuantos M² es: "))
print("Ok.")
cm2 = float(input("Cuanto es el costo por M²: "))

ct = tm2 * cm2
print(f"Bien, he calculado cuanto debes de pagar, bueno tienes que pagar {ct}")
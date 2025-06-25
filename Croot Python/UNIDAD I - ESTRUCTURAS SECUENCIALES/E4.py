"""
    Cobro de estacionamiento por horas:
    Se cobra una tarifa fija por cada hora o fracción de hora que el vehículo esté estacionado.
    Cualquier tiempo extra, aunque sea un minuto, se cuenta como una hora completa.
"""
from math import ceil

print("HOLA, QUISIERA SABER CUANTO TIEMPO ESTUVISTE ESTACIONADO RESPONDE CON CLARIDAD")
he = int(input("Cuantas horas estuiste estacioando?: "))
me = int(input(f"{he}H:(con cuantos minutos?)M: "))
t = float(input("Cuanto es la tarifa por Hora: "))

tt = he + me / 60
hc = ceil(tt)
totalCobrar = hc * t
print()
print(f"ESTIMADO USUARIO, TE HAS QUEDADO {hc} Horas, por lo tanto debes de pagar a caja {totalCobrar} PEN.")
print("GRACIAS POR USAR NUESTRO SERVICIO.")
"""
    Costo de llamada telefónica**
    Entrada: minutos y precio por minuto.
"""

print("HOLA USUARIO, VAMOS A CALCULAR EL COSTO DE TU LLAMADA.")

minutes = float(input("Cuantos minutos estuviste en llamda: "))
priceMinutes = float(input("Digita el precio que vas a pagar por 1 minuto de llamada: "))

pagar = minutes / priceMinutes

print(f"USUARIO, POR HABER TENIDO UNA LLAMADA DE {minutes} MINUTOS, VAS A PAGAR EN TOTAL {pagar} SOLES.")

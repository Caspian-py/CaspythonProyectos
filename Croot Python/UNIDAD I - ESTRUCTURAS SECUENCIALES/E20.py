"""
    **Pago por estancia en hotel**
    Entrada: número de días, precio por noche.
"""

print("CUANTO PAGAR EN ESTANCIA EN HOTEL")

dias = int(input("Cuantos dias te quedaras?: "))
pp = float(input("Precio por Nochre: "))

pt = dias * pp

print(f"Por estar {dias} dias, vas a pagar {pt} soles.")
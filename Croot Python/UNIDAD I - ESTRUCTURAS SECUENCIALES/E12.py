"""
    Cheque de viáticos:
    Calcula el monto total según los días de viaje.
    Se gastan 100 soles diarios en viáticos.
"""

print("CHEQUE DE VIATICOS")

dias = int(input("Cuantos dias Viajaras?: "))
gdf = 100
mt = dias * gdf

print(f"El monto total del cheque si vas a viajar {dias} dias, seria de {mt} soles.")

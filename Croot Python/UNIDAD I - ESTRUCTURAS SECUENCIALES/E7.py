"""
    **Costo de un boleto de autobús**
    Entrada: km por recorrer y precio por km.
"""

print("VAMOS A CALCULAR EL COSTO DE TU BOLETO DE AUTOBUS")

kmR = float(input("Cuantos KM recorriste en el autobus: "))
pKM = float(input("Cuanto es el precio por KM: "))

cb = kmR * pKM

print(f"El Costo que debes de pagar por haber recorrido {kmR} KM es: {cb} soles.")
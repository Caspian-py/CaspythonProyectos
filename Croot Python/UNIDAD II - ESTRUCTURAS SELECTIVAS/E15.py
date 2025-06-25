"""
**Aplicar un descuento según cantidad comprada de productos.**

* 1 a 9: 0%
* 10 a 99: 10%
* 100 o más: 20%
"""

cantP = int(input("Cantidad de productos: "))
costo = float(input("Suma total de los precios: "))
print()
if cantP >= 1 and cantP <=9:
    print("Tu descuento es del 0%.")
    tp = costo - (costo * 0.0)
    print(f"Total a pagar es {tp} soles.")
elif cantP >= 10 and cantP <= 99:
    print("Tu descuento es del 10%.")
    tp = costo - (costo * 0.10)
    print(f"Total a pagar es {tp} soles.")
elif cantP >= 100:
    print("Tu descuento es del 20%.")
    tp = costo - (costo * 0.20)
    print(f"Total a pagar es {tp} soles.")

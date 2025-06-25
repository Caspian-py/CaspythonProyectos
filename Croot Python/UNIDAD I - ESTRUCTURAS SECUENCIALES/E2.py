"""
    Convierte soles peruanos a Dolares, el usuario ingresara la cantidad de soles y el tipo de camnio.
"""



soles = float(input(" Cuantos PEN deseas cambiar a USD: "))
TCambio = float(input("Precio de USD en PEN: "))

usd = soles / TCambio

print(f"Si tienes {soles} PEN y 1 USD es igual a {TCambio} PEN, entonces tienes {usd} USD.")



"""
    **Validar si un número es positivo, negativo o cero.**
"""

numero =  float(input("Numero: "))

if numero < 0:
    print(f"{numero} es negativo.")
elif numero > 0:
    print(f"+{numero} es positivo")
else:
    print(f"{numero} no es positivo tampoco negatico.")
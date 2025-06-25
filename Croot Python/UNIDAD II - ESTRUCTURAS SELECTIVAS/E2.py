"""
    **Verificar si un número es positivo o negativo.**
"""

n = float(input("Numero: "))

if n > 0:
    print(f"+{n} es positivo.")
elif n < 0:
    print(f"{n} es negativo.")
else:
    print(f"{n} no es negativo ni positivo, es nulo.")
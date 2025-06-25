"""
    **Determinar si un número es múltiplo de otro.**
"""

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))

if n1 % n2 == 0:
    print(f"{n1} si es multiplo de {n2}." )
else:
    print(f"{n1} no es multiplo de {n2}.")


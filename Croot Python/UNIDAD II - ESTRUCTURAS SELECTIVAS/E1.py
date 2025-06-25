"""
    **Determinar cuál de dos números es mayor.**
"""

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))

if n1 > n2:
    print(f"El {n1} es mayor que {n2}.")
elif n2 > n1:
    print(f"el {n2} es mayor que {n1}.")
else:
    print(f"{n1} es igual a {n2}")
    
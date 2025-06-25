"""
    **Evaluar si un número está dentro de un rango.**
"""


rmenor = float(input("Rango menor: "))
rmayor = float(input("Rango mayor: "))
print()
n = float(input("Numero: "))


if n >= rmenor and n<=rmayor:
    print(f"{n} esta dentro del rango {rmenor}:{rmayor}.")
else:
    print(f"{n} no esta en el rango {rmenor}:{rmayor}.")


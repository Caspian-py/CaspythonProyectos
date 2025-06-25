"""
    **Cálculo de meses, semanas, días y horas vividas a partir de la edad**
"""

print("TU EDAD EN MESES, SEMANAS, DIAS Y HORAS.")

e = int(input("Dime tu edad: "))
print()

meses = e * 12
semanas = e * 52
dias = e * 365
horas = dias * 24

print("TIEMPO VIVIDO: ")
print()
print(f"Meses: {meses}")
print(f"Semanas: {semanas}")
print(f"Dias: {dias}")
print(f"horas: {horas}")


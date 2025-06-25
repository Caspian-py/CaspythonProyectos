"""
    **Calcular la tabla de multiplicar de un número del 1 al 10.**
"""

numero = int(input("Que tabla de multiplicar quieres ver: "))
print()
print(f"TABLA DE {numero}: ")
for i in range(10):
    print(f"{numero} X {i+1} = {numero * (i+1)}")

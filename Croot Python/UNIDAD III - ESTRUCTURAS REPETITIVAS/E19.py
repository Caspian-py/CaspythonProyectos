"""
    **Leer números hasta que se ingrese un cero y calcular la suma total.**
"""
suma = 0
id = 1
while True:
    numero = float(input(f"Numero ({id}): "))
    suma += numero
    if numero == 0:
        break
    id += 1
print()
print(f"La suma Total es ({suma})")
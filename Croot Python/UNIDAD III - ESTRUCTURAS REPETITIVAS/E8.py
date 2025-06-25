"""
    **Leer 20 números y encontrar el mayor.**
"""
numero = []
caja = 0
for id in range(5):
    num = float(input(f"Numero ({id + 1}): "))
    numero.append(num)
    if num > caja:
        caja = num
print()
print(f"Con funcion max(), el numero mayor es {max(numero)}.")
print(f"Con estructura condicional, el numero mayor es {caja}.")

"""
    **Sumar 10 números introducidos por el usuario.**
"""
sumaT = 0
for c in range(10):
    numero = float(input(f"Numero {c+1}: "))
    sumaT = sumaT + numero

print()
print(f"La suma total es {sumaT}")
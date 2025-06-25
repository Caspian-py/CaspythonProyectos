"""
    **Leer N números y contar cuántos son pares y cuántos impares.**
"""

n = int(input("Valor N: "))
pares = 0
impares = 0
for id in range(n):
    num = int(input(f"Numero ({id + 1}): "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Tienes {pares} numeros pares y {impares} numeros impares.")

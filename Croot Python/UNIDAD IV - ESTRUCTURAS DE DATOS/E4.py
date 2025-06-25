"""
    **Leer 10 números y contar cuántos son mayores que el promedio.**
"""
numeros = []
for id in range(10):
    numero = float(input(f"Numero: ({id + 1}): "))
    numeros.append(numero)

promedio = sum(numeros) / 10
NumerosM = 0
for value in numeros:
    if value >= promedio:
        NumerosM += 1
print()
print(f"Hemos encontrado {NumerosM} numeros mayores del promedio {promedio}.")
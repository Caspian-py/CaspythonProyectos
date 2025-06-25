"""
    **Contar cuántos números positivos se ingresaron de una lista de N.**
"""

cantidad = int(input("Cuantos numeros vas a ingresar: "))
n = []
for i in range(cantidad):
    num = float(input(f"Numero ({i+1})"))
    n.append(num)
cp = 0
for numero in n:
    if numero > 0:
        cp += 1
print()
print(f"Se ingresaron {cp} numeros positivos.")

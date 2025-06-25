"""
    **Algoritmo para validar si una palabra es un palíndromo (ej. "reconocer").**
"""

palabra = input("PALABRA: ").lower().replace(" ","")
print()
if palabra == palabra[::-1]:
    print(f"{palabra[::-1]} = {palabra}, si es una palabra PALINDROMO.")
else:
    print(f"{palabra[::-1]} = {palabra}, no es una palabra PALINDROMO.")

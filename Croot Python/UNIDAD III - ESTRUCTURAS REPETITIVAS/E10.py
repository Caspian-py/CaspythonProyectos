"""
    **Leer 10 edades y determinar cuántos son mayores de edad.**
"""

mEdad = 0
for id in range(10):
    edad = int(input(f"Edad ({id + 1}): "))
    if edad >= 18:
        mEdad += 1

print(f"Hemos encontrado {mEdad} personas mayores de edad.")

"""
    **Clasificar a una persona según su edad:**

    * Menor de 12: niño
    * De 13 a 17: adolescente
    * De 18 a 59: adulto
    * 60 o más: adulto mayor
"""

nombre = str(input("Nombre: "))
edad = int(input("Edad: "))
print()

if edad <= 12:
    print(f"{nombre} es un ninio.")
elif edad >= 13 and edad <= 17:
    print(f"{nombre} es un adolescente.")
elif edad >= 18 and edad <=59:
    print(f"{nombre} es un adulto.")
elif edad >= 60:
    print(f"{nombre} es un adulto mayor.")
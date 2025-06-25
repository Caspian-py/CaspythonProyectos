"""
    **Determinar si una persona es mayor, menor o igual de edad a otra.**
"""

p1 = input("Como te llamas: ")
edad1 = int(input("Tu Edad: "))
print()
p2 = input("Como te llamas: ")
edad2 = int(input("Tu Edad: "))
print("==============================================")
if edad1 > edad2:
    print(f"{p1} es mayor que {p2}.")
elif edad1 < edad2:
    print(f"{p2} es mayor que {p1}.")
else:
    print(f"{p1} y {p2} tienen la misma edad.")

print("==============================================")

if edad1 > edad2:
    print(f"{p1} es mayor que {p2}.")
elif edad1 < edad2:
    print(f"{p1} es menor que {p2}.")
elif edad1 == edad2:
    print(f"{p1} y {p2} tienen la misma edad.")

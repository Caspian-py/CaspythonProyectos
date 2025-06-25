"""
    **Determinar si una persona puede votar.**
    Si tiene 18 años o más, puede votar.
"""

edad = int(input("Edad: "))

if edad >= 18:
    print(f"Tienes {edad} anios, puedes votar.")
else:
    print(f"Tienes {edad} anios, aun no puedes votar.")

    

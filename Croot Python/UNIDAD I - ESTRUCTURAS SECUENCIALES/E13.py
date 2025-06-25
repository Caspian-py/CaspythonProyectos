"""
    Potencia eléctrica:
    Ingresa corriente y resistencia. Calcula la potencia con: P = R * I**2
"""

print("POTENCIA ELECTRICA")

i = float(input("Ingresa la corriente(I) Amperios: "))
r = float(input("Ingresa la Resistencia(R) Ohmios: "))

p = r * (i**2)

print(f"La potencia electrica(P) seria: {p} Vatios")

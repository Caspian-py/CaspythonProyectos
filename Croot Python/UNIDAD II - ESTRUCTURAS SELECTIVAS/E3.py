"""
    **Calcular cuánto se debe pagar por lápices.**
    Si compra 1000 o más: 0.85 c/u. Si no,  0.90 c/u.
"""

cl = int(input("Cuantos lapices vas a comprar: "))

if cl >= 1000:
    pt = cl * 0.85
else:
    pt = cl * 0.90

print(f"Total a pagar por comprar { cl} es: {pt} soles.")


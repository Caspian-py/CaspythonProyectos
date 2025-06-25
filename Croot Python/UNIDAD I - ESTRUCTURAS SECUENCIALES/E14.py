"""
    Calcula el volumen y área de un cilindro
    Pide el radio y la altura y calcula el volumen y área superficial del cilindro.
    Volumen = π × r² × h
    Área = 2 × π × r × (r + h)
"""
import math

print("VOLUMEN Y AREA DE UN CILINDRO.")

r = float(input("Radio(r): "))
h = float(input("Altura(h): "))
pi = math.pi
v = pi * r**2 * h
print(f"El volumen del cilindro, con radio(r) {r} y altura(h) {h} es {v}")
a = 2 * pi * r * (r + h)
print(f"El area de del cilindro, con radio(r) {r} y altura(h) {h} es {a}")

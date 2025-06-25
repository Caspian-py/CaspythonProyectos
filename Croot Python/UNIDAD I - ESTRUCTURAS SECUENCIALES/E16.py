"""
    Convierte temperatura de Fahrenheit a Celsius y Kelvin
    Pide una temperatura en Fahrenheit y muestra su equivalente en Celsius y Kelvin.
    Celsius = (Fahrenheit - 32) × 5/9
    Kelvin = Celsius + 273.15
"""

print("FAHRENHEIt A CELSIUS Y KELVIN")

f = float(input("Fahrenheit(°F): "))

c = (f - 32) * 5 / 6
k = c + 273.15

print(f"{f}°F en Celcius es {c}°C")
print(f"{f}°F en Kelvin es {k}°°K")

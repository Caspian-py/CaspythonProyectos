"""
    Calcula el Area de un triangulo.
    Formula: (base * altura) / 2
"""

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo usando la fórmula:
    (base * altura) / 2
    """
    return (base * altura) / 2

def pedir_float(mensaje: str) -> float:
    """
    Solicita un número flotante al usuario, validando la entrada.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("El valor debe ser mayor que cero.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

# Programa principal
print("CÁLCULO DEL ÁREA DE UN TRIÁNGULO")
print("-" * 40)

base = pedir_float("Ingrese la base del triángulo: ")
altura = pedir_float("Ingrese la altura del triángulo: ")

area = calcular_area_triangulo(base, altura)

print(f"\n🔺 El área del triángulo con base {base} y altura {altura} es: {area:.2f} unidades²")

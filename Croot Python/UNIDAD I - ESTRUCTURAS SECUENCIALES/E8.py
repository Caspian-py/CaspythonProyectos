"""
    Tiempo de viaje en bicicleta
    Entrada: distancia y velocidad constante.
"""

print("QUERIDO USUARIO, VAMOS A CALCULAR TU TIEMPO DE VIAJE EN BICICLETA.")

dv = float(input("Ingresa la distancia de tu viaje en KM: "))
vc = float(input("Cual sera la velocidad con la que viajaras: "))

tv = dv / vc

print(f"El tiempo que te tomara viajar {dv} KM si viajas a una velocidad de {vc} KM/H es de {tv} Horas y minutos.")
"""
    Convierte horas, minutos y segundos a segundos totales
    Pide horas, minutos y segundos, y muestra el tiempo total en segundos.
    Total segundos = (horas × 3600) + (minutos × 60) + segundos
"""

print("CONVERTIR UNA HORA A SEGUNDOS.")

h = int(input("Hora: "))
m = int(input("Minuto: "))
s = int(input("Segundos: "))

ts = (h * 3600) + (m * 60) + s

print(f"La hora que ingresaste fue {h}:{m}:{s}, en segundos seria {ts} seg.")


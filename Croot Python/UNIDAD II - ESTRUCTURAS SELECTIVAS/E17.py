"""
    **Clasificar la temperatura:**

    * < 0: congelante
    * 0–10: fría
    * 11–25: templada
    * > 25: calurosa
"""

temperatura = float(input("Temperatura (°C): "))

if temperatura < 0:
    print(f"La temperatura {temperatura} °C, es congelante.")
elif temperatura >= 0 and temperatura <= 10:
    print(f"La temperatura {temperatura} °C, es fria.")
elif temperatura >= 11 and temperatura <= 25:
    print(f"La temperatura {temperatura} °C, es templada.")
elif temperatura > 25:
    print(f"La temperatura {temperatura} °C, es calurosa.")

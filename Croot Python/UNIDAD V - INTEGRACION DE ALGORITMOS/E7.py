"""
    **Juego de adivinanza con intentos limitados:**
    El usuario tiene 5 intentos para adivinar un número aleatorio entre 1 y 100.
"""
import random
aleatorio = random.randint(1, 100)
print("ADIVINA EL NUMERO DEL 1 AL 100")
i = 1
while i <= 5:
    print(f"Intento {i}:")
    n = int(input("Numero: "))
    if n == aleatorio:
        print("FElicidades, Haz acertado!!")
        break
    elif i == 5:
        print("Has perdido, tus intentos se han acabado.")
        print(f"El Numero aleatorio era {aleatorio}.")
        break
    else:
        i += 1
    

    
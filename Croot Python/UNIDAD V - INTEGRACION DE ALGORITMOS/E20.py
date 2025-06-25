"""
    **Juego básico de piedra, papel o tijera contra la IA.**
"""
import os
import random
def ia():
    n = random.randint(1,3)
    if n == 1:
        return "piedra"
    elif n == 2:
        return "papel"
    elif n == 3:
        return "tijera"
    
while True:
    os.system("cls")

    print("-"*17,"✊ 🖐  ✌ ","-"*17)
    print()
    print("(Salir 'exit') PIEDRA✊ PAPEL🖐 TIJERA✌")
    print()
    usser = input("-> ").strip().lower()
    iaj = ia()
    if usser == "salir":
        break

    if usser == "piedra":

        print(f"Tu: ✊")

        if iaj == "piedra":
            print(f"PC: ✊")
            print("Esto es un Empate.")
        elif iaj == "tijera":
            print(f"PC: ✌")
            print("Ganasta!!")
        elif iaj == "papel":
            print(f"PC: 🖐")
            print("Has Perdido!!")

    elif usser == "papel":

        print(f"Tu: 🖐")

        if iaj == "papel":
            print(f"PC: 🖐")
            print("Esto es un Empate.")
        elif iaj == "piedra":
            print(f"PC: ✊")
            print("Has Ganado!!")
        elif iaj == "tijera":
            print(f"PC: ✌")
            print("Has Perdido!!")

    elif usser == "tijera":

        print(f"Tu: ✌")

        if iaj == "tijera":
            print(f"PC: ✌")
            print("Esto es un Empate.")
        elif iaj == "papel":
            print(f"PC: 🖐")
            print("Has Ganado!!")
        elif iaj == "piedra":
            print(f"PC: ✊")
            print("Has Perdido!!")

    input("...")





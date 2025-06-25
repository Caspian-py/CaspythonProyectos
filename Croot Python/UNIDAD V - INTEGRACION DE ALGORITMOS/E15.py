"""
    **Simulador de boletos de cine (con butacas numeradas y ocupación).**
"""
import os
import time
sala = [
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True]
]

def mostrarSala():
    print("=" * 40)
    print("SALA")
    print("=" * 40)
    print()
    
    print(" ", end="")
    for i in range(len(sala[0])):
        print(f"{i + 1:>4}", end="")
    print()
    for i, fila in enumerate(sala):
        letrafil = chr(65 + i )
        print(f"{letrafil}  ", end="")
        for asiento in fila:
            if asiento:
                print("[L] ", end="")
            else:
                print("[X] ", end="")
        print()

def reservar():
    os.system("cls")
    mostrarSala()
    while True:
        time.sleep(3)
        os.system("cls")
        mostrarSala()
        print()
        print("-" * 40)
        print("Seleccione una butaca (ej: B3) o presiona Enter para salir.")
        entrada = input("-> ").strip().upper()
        if entrada == "":
            os.system("cls")
            return
        
        fila = entrada[0]
        columna = entrada[1]

        if len(entrada) != 2:
            print("La butaca debe estar compuesto de 1 letra y 1 numero.")
            time.sleep(3)
            continue
        if (ord(fila) - 65) < 0 or (ord(fila) - 65) > len(sala):
            print("No hemos encontrado la fila, intenta de nuevo.")
            time.sleep(3)
            continue
        if not columna.isdigit():
            print("Debes ingresar un numero despues de la letra.")
            time.sleep(3)
            continue
        if columna.isdigit():
            if not 1 <= int(columna) <= len(sala[0]):
                print("No hemos encontrado la columna, intenta nuevamente.")
                time.sleep(3)
                continue

        f = ord(fila) - 65
        c = int(columna) - 1
        if sala[f][c] == True:
            sala[f][c] = False
            print(f"Butaca {entrada} reservada con exito!.")
        else:
            print(f"Butaca {entrada} ya esta ocupado.")



def main():

    while True:
        os.system("cls")
        mostrarSala()
        print()
        print("OPCIONES: ")
        print("1) Reservar")
        print()
        print("-" * 40)
        option = input("-> ")
        if not option.isdigit():
            break
        op = int(option)
        if op == 1:
            os.system("cls")
            reservar()
            






main()
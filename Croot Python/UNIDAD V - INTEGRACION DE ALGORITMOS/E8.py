"""
    **Simulación de cajero automático:**

    * Ingreso con PIN.
    * Ver saldo, retirar, depositar.
    * Validaciones para errores comunes.
"""
import os
cuenta = []
print("CREAR CUENTA DE BANCO")
for _ in range(1):
    while True:
        nombre = str(input("NOMBRE: "))
        if len(nombre) <= 2 or nombre == "":
            print("nombre de usuario, no valido.")
        else:
            saldo = float(input("SALDO: "))
            break
    cuenta.append(
        {
            "nombre": nombre,
            "saldo": saldo
        }
    )


def mostrar():
    print("DATOS DE LA CUENTA")
    print("-" * 40)
    for datos in cuenta:
        print(f"Nombre: {datos['nombre'].capitalize()}")
        print(f"Saldo: {datos['saldo']} soles.")
        print("-" * 40)        
def menu():
    while True:
        os.system("cls")
        mostrar()
        print("OPCIONES")
        print("-" * 40)
        print("-> RETIRAR")
        print("-> DEPOSITAR")
        print("-> SALIR")
        print("-" * 40)
        option = input("OPCION -> ").lower()
        if option in ("retirar", "depositar", "salir"):
            if option == "salir":
                break
            elif option == "retirar":
                os.system("cls")
                mostrar()
                while True:
                    retiro = float(input("RETIRAR: ")) 
                    if retiro <= cuenta[0]['saldo']:
                        cuenta[0]["saldo"] -= retiro
                        break
                    else:
                        print("Saldo Insuficiente, intente nuevamente.")
            elif option == "depositar":
                os.system("cls")
                mostrar()
                deposito = float(input("DEPOSITAR: "))
                cuenta[0]['saldo'] += deposito
        else:
            print("Opcion no valida, intente nuevamente.")
        

os.system("cls")
menu()

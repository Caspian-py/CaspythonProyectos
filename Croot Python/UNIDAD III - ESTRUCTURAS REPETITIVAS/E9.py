"""
    **Determinar si un número es primo (mediante ciclo de divisores).**
"""

numero = int(input("Numero: "))

if numero >= 2:
    primo = True
    for i in range(2, (numero - 1), 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} es primo.")
    else:
        print(f"No es primo.")




else:
    print(f"{numero} no es primo.")
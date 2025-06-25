"""
    **Simular un cajero:**
    Si el usuario tiene saldo suficiente, permitir retiro; si no, denegar.
"""

saldo = float(input("Saldo de tarjeta para la simulacion: "))
print()
retirar = float(input("Saldo a retirar: "))

if retirar <= saldo:
    saldo = saldo - retirar
    print(f"Saldo: {saldo}")
    print("Retiro realizado con exito.")
elif retirar > saldo:
    print(f"Saldo: {saldo}")
    print("Retirno denegado por saldo insuficiente.")

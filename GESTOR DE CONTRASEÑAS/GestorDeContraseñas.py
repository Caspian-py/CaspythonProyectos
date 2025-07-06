"""
    🔹 3. Gestor de contraseñas
    •	Funcionalidades: guardar contraseñas encriptadas, buscarlas por servicio
    •	Módulos: hashlib o cryptography, json
    •	Aprendes: hashing, manejo seguro de datos, persistencia de archivos.
"""

import hashlib, os

def clear():
    os.system("cls" if os.name == "nt" else "clear")




def main():
    while True:
        clear()
        print("INICIAR SESION")
        print("REGISTRARSE")
        print("SALIR")
        
        opt = input("Ingresa tu opcion: ").strip().lower()

        if opt in ("iniciar sesion", "iniciar"):
            input("def iniciar_sesion() ")
        elif opt in ("registrarse", "registrarme", "registrar"):
            input("def registrar() ")
        elif opt in ("salir", ""):
            break
        else:
            input("Opcion no valida. ")
main()



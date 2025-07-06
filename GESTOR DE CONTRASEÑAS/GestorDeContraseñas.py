"""
    🔹 3. Gestor de contraseñas
    •	Funcionalidades: guardar contraseñas encriptadas, buscarlas por servicio
    •	Módulos: hashlib o cryptography, json
    •	Aprendes: hashing, manejo seguro de datos, persistencia de archivos.
"""

import hashlib, os, json
from getpass import getpass



def clear():
    os.system("cls" if os.name == "nt" else "clear")

def import_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
usuarios = import_usuarios()

def guardar_usuarios(usuarios):
    try:
        with open('usuarios.json', 'w') as f:
            json.dump(usuarios, f, indent=4)
            return True
    except (PermissionError, OSError):
        return False
    
def registrar():
    while True:
        clear()
        print("REGISTRAR NUEVO USUARIO")
        print()
        validacion = False
        nombre = input("USUARIO: ").strip().lower()
        if not nombre == "":
            if len(nombre) < 4:
                input("El nombre es muy corto. ")
                continue
            else:
                validacion = True

        passw = getpass("CLAVE MAESTRA: ").strip()
        if not passw == "":
            if len(passw) < 6:
                input("La contrasenia es muy insegura, maximo 6 digitos ")
                continue
            else:
                validacion = True

        print()
        if validacion:
            clave_maestra = hashlib.sha256(passw.encode()).hexdigest()
            usuarios.append(
                {
                    "usuario": nombre,
                    "claveM": clave_maestra
                }
            )
            if guardar_usuarios(usuarios):
                input("USUARIO REGISTRADO CORRECTAMENTE ")
                return
            else:
                input("ERROR AL REGISTRAR NUEVO USUARIO ")
        if input("CONTINUAR? (s/n): ").lower().strip() == "n":
            return
        
def iniciar_sesion():
    while True:
        clear()
        print("INICIAR SESION")
        print()
        usuario = input("NOMBRE DE USUARIO: ").lower().strip()
        passw = getpass("CLAVE MAESTRA: ").strip()
        clave_maestra = hashlib.sha256(passw.encode()).hexdigest()
        for id, u in enumerate(usuarios):
            if usuario == u['usuario'] and clave_maestra == u['claveM']:
                main_usuario(id)
                return
        
        input("CREDENCIALES NO REGISTRADAS")
        if input("SALIR (s/n): ").lower().strip() == "s":
            return
def main_usuario(id):
    clear()
    print(f"BIENVENIDO {usuarios[id]['usuario'].upper()}")
    input()
    return

def main():
    while True:
        clear()
        print(usuarios)
        print("INICIAR SESION")
        print("REGISTRARSE")
        print("SALIR")
        
        opt = input("Ingresa tu opcion: ").strip().lower()

        if opt in ("iniciar sesion", "iniciar"):
            iniciar_sesion()
        elif opt in ("registrarse", "registrarme", "registrar"):
            registrar()
        elif opt in ("salir", ""):
            break
        else:
            input("Opcion no valida. ")
main()



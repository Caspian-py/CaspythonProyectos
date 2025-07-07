"""
    🔹 3. Gestor de contraseñas
    •	Funcionalidades: guardar contraseñas encriptadas, buscarlas por servicio
    •	Módulos: hashlib o cryptography, json
    •	Aprendes: hashing, manejo seguro de datos, persistencia de archivos.
"""

import hashlib, os, json
from getpass import getpass

centro = os.get_terminal_size().columns



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

def import_pwd(ussid):
    global list_claveM
    try:
        clave = str(usuarios[ussid]['claveM'])
        with open(f'{clave}.json', 'r') as f:
            list_claveM = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        list_claveM = []

def guardar_pwd(ussid):
    input(usuarios[ussid])
    try:
        clave = str(usuarios[ussid]['claveM'])

        with open(f'{clave}.json', 'w') as f:
            json.dump(list_claveM, f, indent=4)
    except (PermissionError, OSError):
        input("ERROR AL GUARDAR LAS CONTRASEÑAS ")

def registrar():
    while True:
        clear()
        print("📝 REGISTRAR NUEVO USUARIO 📝").center(centro)
        print()
        validacion = False
        print("👤 USUARIO:")
        nombre = input(">>> ").strip().lower()
        if not nombre == "":
            if len(nombre) < 4:
                input("⚠️ EL NOMBRE ES MUY CORTO ")
                continue
            else:
                validacion = True
        print("🔑 CLAVE MAESTRA:")
        passw = getpass(">>> ").strip()
        if not passw == "":
            if len(passw) < 6:
                input("⚠️ MINIMO 6 CARACTERES ")
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
                input("✅ USUARIO REGISTRADO CORRECTAMENTE ")
                return
            else:
                input("❌ ERROR AL REGISTRAR NUEVO USUARIO ")
        if input("🔁 CONTINUAR? (s/n): ").lower().strip() == "n":
            return
        
def iniciar_sesion():
    while True:
        clear()
        print("🔐 INICIAR SESION 🔐".center(centro))
        print()
        print("👤 NOMBRE DE USUARIO:")
        usuario = input(">>> ").lower().strip()
        print("CLAVE MAESTRA:")
        password = getpass(">>> ").strip()
        clave_maestra = hashlib.sha256(password.encode()).hexdigest()
        for id, u in enumerate(usuarios):
            if usuario == u['usuario'] and clave_maestra == u['claveM']:
                ussid = id
                import_pwd(ussid)
                main_usuario(ussid)
                return
        
        print("CREDENCIALES NO REGISTRADAS")
        if input("SALIR (s/n): ").lower().strip() == "s":
            return

def main_usuario(ussid):
    clear()
    print(f"BIENVENIDO {usuarios[ussid]['usuario'].upper()}")
    mostrar_list_pwd(ussid)
    print()
    print("NUEVO")
    print("MODIFICAR")
    print("ELIMINAR")
    print()
    print("CERRAR SESION")
    opt = input().strip().lower()
    if opt in ("nuevo", "new", "agregar"):
        agregar_new_pwd(ussid)

def mostrar_list_pwd(ussid):
    print("LISTA DE CONTRASEÑAS GUARDADAS")
    if len(list_claveM) == 0:
        print("AUN NO TIENES GUARDADA NINGUNA CONTRASEÑA")
    else:
        print(list_claveM)

def agregar_new_pwd(ussid):
    service = input("SERVICIO: ").strip().lower()
    usser = input("USUARIO: ").strip()
    pwd = getpass("CONTRASEÑA: ").strip()

    list_claveM.append(
        {
            'service': service,
            'usser': usser,
            'pwd': pwd
        }
    )
    guardar_pwd(ussid)
    input("AGREGADO CORRECCTAMENTE")



def main():
    while True:
        clear()
        print(usuarios)
        print("-" * 30)
        print("🔐 INICIAR SESION")
        print("📝 REGISTRARSE")
        print("❌ SALIR")
        print("-" * 30)
        opt = input(">>> ").strip().lower()

        if opt in ("iniciar sesion", "iniciar"):
            iniciar_sesion()
        elif opt in ("registrarse", "registrarme", "registrar"):
            registrar()
        elif opt in ("salir", ""):
            break
        else:
            input("⚠️ OPCION NO VALIDA")
main()



"""
    🔹 3. Gestor de contraseñas
    •	Funcionalidades: guardar contraseñas encriptadas, buscarlas por servicio
    •	Módulos: hashlib o cryptography, json
    •	Aprendes: hashing, manejo seguro de datos, persistencia de archivos.
"""

import hashlib, os, json
from getpass import getpass
from cryptography.fernet import Fernet


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
    try:
        clave = str(usuarios[ussid]['claveM'])

        with open(f'{clave}.json', 'w') as f:
            json.dump(list_claveM, f, indent=4)
    except (PermissionError, OSError):
        input("ERROR AL GUARDAR LAS CONTRASEÑAS ")

def registrar():
    while True:
        clear()
        print("📝 REGISTRAR NUEVO USUARIO 📝".center(centro))
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
            key = Fernet.generate_key().decode()

            usuarios.append(
                {
                    "usuario": nombre,
                    "claveM": clave_maestra,
                    "key": key
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
        print("🔑 CLAVE MAESTRA:")
        password = getpass(">>> ").strip()
        clave_maestra = hashlib.sha256(password.encode()).hexdigest()
        for id, u in enumerate(usuarios):
            if usuario == u['usuario'] and clave_maestra == u['claveM']:
                ussid = id
                import_pwd(ussid)
                main_usuario(ussid)
                return
        
        print("❌ CREDENCIALES NO REGISTRADAS")
        if input("SALIR (s/n): ").lower().strip() == "s":
            return

def main_usuario(ussid):
    while True:
        clear()
        print(f"👋 BIENVENIDO {usuarios[ussid]['usuario'].upper()} 👋")
        mostrar_list_pwd(ussid)
        print()
        print("➕ NUEVO")
        print("✏️ MODIFICAR")
        print("🗑️ ELIMINAR")
        print("👀 VER CONTRASEÑA")
        print()
        print("🔓 CERRAR SESION")
        print("-" * 40 )
        opt = input("📌 OPCION: ").strip().lower()
        if opt in ("nuevo", "new", "agregar"):
            agregar_new_pwd(ussid)
        elif opt in ("modificar", "actualizar"):
            main_modificar_pwd(ussid)
        elif opt in ("eliminar", "borrar", "delete"):
            main_eliminar_pwd(ussid)
        elif opt in ("cerrar", "cerrar sesion"):
            return

def mostrar_list_pwd(ussid):
    print("-" * 40 )
    print("🔐 LISTA DE CONTRASEÑAS GUARDADAS 🔐")
    print("-" * 40 )
    if len(list_claveM) == 0:
        print("⚠️ AUN NO TIENES CONTRASEÑAS GUARDADAS")

    else:
        print(f"{'ID':^4} | {'SERVICIO':^5}")
        print("-" * 40)
        for id, f in enumerate(list_claveM):
            print(f"{(id + 1):^4} | {f['service']:^5}")
            print("-" * 40)

def agregar_new_pwd(ussid):
    while True:
        clear()
        print("REGISTRANDO CONTRASEÑA PARA GUARDAR".center(centro))
        print("PARA CANCELAR INGRESE 'cancenlar' EN SERVICIO")
        
        print("SERVICIO:")
        service = input(">>> ").strip()
        if service == "cancelar" or service == "":
            return
        
        print("USUARIO: ")
        usser = input(">>> ").strip()
        if usser == "":
            input("NOMBRE DE USUARIOS INVALIDO")
            continue
        
        print("CONTRASEÑA:")
        pwd = getpass(">>> ").strip()
        print("REPITE UNA VEZ MAS:")
        if getpass(">>> ").strip() != pwd:
            input("CONTRASEÑAS DIFERENTES, POR FAVOR VUELVE A INTENTARLO DE NUEVO.")
            continue

        fernet = Fernet(usuarios[ussid]['key'].encode())
        pwdC = fernet.encrypt(pwd.encode())

        pwdH = hashlib.sha256(pwd.encode()).hexdigest()

        if any(usser == u['usser'] and pwdH == u['pwdH'] for u in list_claveM):
            input("USUARIO Y CONTRASEÑA YA ESTAN REGISTRADAS.")
            continue
        else:
            list_claveM.append(
                {
                    'service': service.upper(),
                    'usser': usser,
                    'pwdC': pwdC.decode(),
                    'pwdH': pwdH
                }
            )
            guardar_pwd(ussid)
            input("AGREGADO CORRECCTAMENTE")
            return
        
def modificar_pwd(ussid, idm):
    while True:
        clear()
        print("MODIFICANDO")
        print("ingresa cancelar o enter para salir")

        print("SERVICIO: ")
        service = input(">>> ").strip()
        if service == "cancelar" or service ==  "":
            return
        
        print("USUARIO NUEVO:")
        usser = input(">>> ").strip()
        if usser == "":
            input("NOMBRE DE USUARIO INVALIDO")
            continue

        print("CONTRASEÑA NUEVA:")
        pwd = getpass(">>> ").strip()
        print("REPITE UNA VEZ MAS: ")
        if getpass(">>> ").strip() != pwd:
            input("CONTRASEÑAS DIFERENTES, POR FAVOR VUELVE A INTENTARLO DE NUEVO. ")
            continue
        fernet = Fernet(usuarios[ussid]['key'].encode())
        pwdC = fernet.encrypt(pwd.encode())

        pwdH = hashlib.sha256(pwd.encode()).hexdigest()

        if any(usser == u['usser'] and pwdH == u['pwdH'] for u in list_claveM):
            input("USUARIO Y CONTRASEÑA YA ESTAN REGISTRADOS.")
            continue
        else:
            print("DIGITA LA CLAVE MAESTRA PARA GUARDAR LOS CAMBIOS (solo 1 intento): ")
            clave = getpass(">>> ").strip()
            claveM = hashlib.sha256(clave.encode()).hexdigest()
            if claveM == usuarios[ussid]['claveM']:
                list_claveM[idm]['service'] = service.capitalize()
                list_claveM[idm]['usser'] = usser
                list_claveM[idm]['pwdC'] = pwdC.decode()
                list_claveM[idm]['pwdH'] = pwdH
                guardar_pwd(ussid)
                input("MODIFICADO CORRECTAMENTE.")
                return
            else:
                input("CLAVE MAESTRA ICNORRECTA.")
                return
        
def main_modificar_pwd(ussid):
    while True:
        clear()
        print("MODIFICAR CONTRASEÑA".center(centro))
        mostrar_list_pwd(ussid)
        print("DIGITA EL ID A MODIFICAR (0 para salir):")
        try:
            id = int(input(">>> ").strip())
            if id in (0, ""):
                return
            if id < 0 or id > len(list_claveM):
                raise ValueError
        except ValueError:
            input("ID NO VALIDO ")
            continue
        idm = id - 1
        modificar_pwd(ussid, idm)
        if input("DESEAS MODIFICAR MAS? (s/n): ").strip() == "n":
            return
        
def eliminar_pwd(ussid, ide):
    while True:
        clear()
        print("ELIMINANDO: ")
        print("INGRESA LA CLAVE MAESTRA PARA ELIMINAR (solo 1 intento): ")
        clave = getpass(">>> ").strip()
        claveM = hashlib.sha256(clave.encode()).hexdigest()
        if claveM == usuarios[ussid]['claveM']:
            list_claveM.pop(ide)
            guardar_pwd(ussid)
            input("ELIMINADO CORRECTAMENTE")
            return
        else:
            input("CLAVE MAESTRA INCORRECTA")
            return

def main_eliminar_pwd(ussid):
    while True:
        clear()
        print("ELIMINAR CONTRASEÑA".center(centro))
        mostrar_list_pwd(ussid)
        print("DIGITA EL ID A ELIMINAR (O para salir): ")
        try:
            id = int(input(">>> ").strip())
            if id in (0, ""):
                return
            if id < 0 or id > len(list_claveM):
                raise ValueError
        except ValueError:
            input("ID NO VLAIDO")
            continue
        ide = id - 1
        eliminar_pwd(ussid, ide)
        if input("DESEAS ELIMINAR MAS? (s/n): ").strip() == "n":
            return



def main():
    while True:
        clear()
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



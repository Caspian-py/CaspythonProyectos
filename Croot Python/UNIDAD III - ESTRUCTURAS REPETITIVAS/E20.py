"""
    **Simular el ingreso de contraseñas hasta que el usuario acierte.**
"""
usuario = "c-root"
password = "202523"

while True:
    user = str(input(f"Usuario: "))
    passw = str(input(f"Password: "))
    if user == usuario and passw == password:
        print(f"Bienvenido {usuario.upper()}!!.")
        break
    else:
        print("Credenciales invalidas, vuelva a intentarlo.")
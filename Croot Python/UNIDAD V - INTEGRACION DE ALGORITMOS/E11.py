"""
    **Sistema de reservas de sala de reuniones.**
"""
import os
reservas = []
def reservar():
    print("RESERVAR:")
    print("-" * 40)
    nombre = input("Nombre: ").capitalize()
    
        
    
    while True:
            dia = int(input("Dia: "))
            hora = int(input("Hora: "))
            ocupado = False
            for reserva in reservas:
                if reserva['dia'] == dia and reserva['hora'] == hora:
                    ocupado = True
                    break
            if ocupado:
                print(f"Dia {dia} y hora {hora} ocupado, ingrese otro dia.")
            else:
                break
                
    while True:
        duracion = int(input("Duracion max(3h): "))
        if duracion < 4:
            break
        else:
            print("Intentalo nuevamente, maximo 3 horas.")

    reservas.append(
        {
            "nombre": nombre,
            "dia": dia,
            "hora": hora,
            "duracion": duracion
        }
    )

def delete():
    print("ELIMINAR RESERVA")
    nombre = input("Nombre: ").capitalize()
    dia = int(input("Dia: "))
    hora = int(input("Hora: "))
    encontrado = False
    for reserva in reservas:
        if reserva["nombre"] == nombre and reserva["dia"] == dia and reserva["hora"] == hora:
            reservas.remove(reserva)
            break
    if not encontrado:
        print("Reserva no encontrado.")

            

def mostrar():
    print("RESERVAS")
    print("-" * 40)
    for reserva in reservas:
        print(f"Nombre: {reserva['nombre']}")
        print(f"Dia: {reserva["dia"]}")
        print(f"Hora: {reserva['hora']}")
        print(f"Duracion: {reserva['duracion']}")
        print("-" * 40)

def menu():
    while True:
        os.system("cls")
        mostrar()
        print()
        print("OPCIONES:")
        print("-" * 40)
        print("-> RESERVAR")
        print("-> ELIMINAR RESERVA")
        print("-> SALIR")
        print("-" * 40)
        option = input("-> ").lower()
        if option in ("reservar", "eliminar reserva", "salir"):
            match option:
                case "reservar":
                    os.system("cls")
                    mostrar()
                    reservar()
                case "eliminar reserva":
                    os.system("cls")
                    mostrar()
                    delete()
                case "salir":
                    break
        else:
            print("OPCION NO VALIDA.")

menu()
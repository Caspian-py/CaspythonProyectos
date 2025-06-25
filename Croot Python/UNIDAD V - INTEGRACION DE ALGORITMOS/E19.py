"""
    **Gestor de tareas pendientes (añadir, mostrar, eliminar).**
"""

import os
import random
tareas = []
"""     {
        "tarea": "aprender python",
        "estado": False
    }
] """

def mostrarTareas():

    for tarea in tareas:
        print(f" CodT({tarea['cod']}) {tarea['tarea']} {"🟢" if tarea['estado'] == True else "🔴"}")

def generadorCod():
    existe = False
    while True:
        cod = random.randint(100,999)
        for tarea in tareas:
            if cod == tarea['cod']:
                existe = True
                break
        if existe == False:
            return cod

def nuevaTarea():
    os.system("cls")
    print("NUEVA TAREA")
    print("-" * 40)
    mostrarTareas()
    print("-" * 40)
    print()
    print("Para Salir Digite 'salir'.")
    tarea = input("-> ").strip().capitalize()
    
    codigo = generadorCod()

    if tarea.lower() == "salir":
        return
    else:
        tareas.append(
            {
                "cod": codigo,
                "tarea": tarea,
                "estado": False
            }
        )
        return
    
def tareaRealizada():
    while True:
        os.system("cls")
        print("MARCAR TAREA REALIZADA")
        print("-" * 40)
        mostrarTareas()
        print("-" * 40)
        print()
        print("Para Salir digite 'salir'.")
        marcar = input("CodT: ").strip().lower()    
        if marcar == "salir":
            return
        if marcar.isdigit():
            if len(marcar) == 3:
                break
            else:
                print("El codigo debe tener solo 3 digitos (###).")
                input()
        else:
            print("El codigo debe contener solo numeros del 1-9 (###).")
            input()
    existe = False
    for tarea in tareas:
        if int(marcar) == tarea['cod']:
            existe = True
            tarea['estado'] = True
    if existe == False:
        print(f"No hemos encontrado una tarea con el CodT({marcar}).")
        input()
        return

def eliminarTarea():
    while True:
        os.system("cls")
        print("ELIINAR TAREA")
        print("-" * 40)
        mostrarTareas()
        print("-" * 40)
        print()
        print("Para Salir Digite 'salir'.")
        eliminar = input("CodT: ").strip().lower()
        if eliminar == "salir":
            return
        if eliminar.isdigit():
            if len(eliminar) == 3:
                break
            else:
                print("El codigo debe tener solo 3 digitos (###).")
                input()
        else:
            print("El codigo debe contener solo numeros del 1-9 (###).")
            input()
    existe = False
    for tarea in tareas:
        if int(eliminar) == tarea['cod']:
            existe = True
            tareas.remove(tarea)
            return
    if existe == False:
        print(f"No hemos encontrado una tarea con el CodT({eliminar})")
        input()
        return

def main():
    while True:
        os.system("cls")
        print("GESTOR DE TAREAS")
        print("-" * 40)
        mostrarTareas()
        print("-" * 40)
        print()
        print("1) AÑADIR TAREA")
        print("2) MARCAR TAREA REALIZADA")
        print("3) ELIMINAR TAREA")
        print()
        print("0) SALIR")
        print("-" * 40)
        opt = input("Opcion: ").strip()
        if not opt.isdigit():
            print("Opcion no Valida.")
            input()
        else:
            if int(opt) == 0:
                break
            if int(opt) == 1:
                nuevaTarea()
            elif int(opt) == 2:
                tareaRealizada()
            elif int(opt) == 3:
                eliminarTarea()
            else:
                print("Opcion no Valida.")
                input()

main()
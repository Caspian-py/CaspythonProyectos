"""
    1. Administrador de tareas en consola (sin clases)
    •	Módulos útiles: os, json
    •	Aprendes: funciones, listas, lectura/escritura de archivos, estructuras de control.
"""

import json
import os
import random

def clear():
    os.system("cls" if os.name == 'nt' else "clear" )

def ImportarJson():
    try:
        with open("datos.json","r") as file:
            tareas = json.load(file)
            return tareas
    except FileNotFoundError:
        return []
    
tareas = ImportarJson()

def GuardarJson(dato):
    try:
        with open("datos.json", "w") as file:
            json.dump(dato, file, indent=4)
    except ValueError:
        print("Error al crear archivo Json, comuniquese con el desarrollador del programa. ⚠️")

def AgregarTarea():
    while True:
        clear()
        MostrarTareas()
        print()
        print(" " * 8,"AGREGAR UNA NUEVA TAREA 📝"," " * 8)
        print("Para SALIR digite 'salir'.")
        tarea = input("📝 Tarea: ").strip().capitalize()
        if tarea.lower() == 'salir':
            return
        if len(tarea) <= 7:
            print("SU TAREA TIENE POCOS DETALLES, POR FAVOR INGRESE NUEVAMENTE CON MAS DETALLES. ⚠️")
            input()
            continue

        else:
            existe = False
            for t in tareas:
                if tarea.lower() == t['tarea'].lower():
                    existe = True
            if existe == False:
                tareas.append(
                    {
                        "tarea": tarea,
                        "estado": False,
                    }
                )
            else:
                print("NO SE PUEDEN REPETIR LAS TAREAS. ⚠️")
                input()
    
def MarcarTarea():
    while True:
        clear()
        MostrarTareas()
        print()
        print(" " * 8,"MARCAR COMO COMPLETADO ✅"," " * 8)
        print("Para SALIR digite '0'.")
        
        try:
            marcar = int(input("ID: "))
        except ValueError:
            print("ID NO VALIDO. ⚠️")
            input()
            continue
        if marcar == 0:
            return

        if marcar > len(tareas) or marcar < 0:
            print("ID NO ENCONTRADO. ⚠️")
            input()
        else:
            if tareas[marcar - 1]['estado'] == True:
                print("LA TAREA YA ESTA MARCADA COMO REALIZADA. ⚠️")
                input()
            else:
                tareas[marcar - 1]['estado'] = True
                return

def EliminarTarea():
    while True:
        clear()
        MostrarTareas()
        print()
        print(" " * 12, "ELIMINAR TAREA 🗑️", "" * 12)
        print("Para SALIR Digite '0'.")

        try:
            eliminar = int(input("ID: "))
        except ValueError:
            print("ID NO VALIDO. ⚠️")
            input()
            continue
        if eliminar == 0:
            return
        if eliminar > len(tareas) or eliminar < 0:
            print("ID NO ENCONTRADO. ⚠️")
            input()
        else:
            print()
            print("SI ESTAS SEGURO DE ELIMINAR LA TAREA DIGITA EL CODIGO CORRECTAMENTE.")
            codigo = random.randint(100,999)
            print(f"COD: {codigo}")
            print()
            try:
                validacion = int(input("COD: "))
            except ValueError:
                return
            if validacion == codigo:
                tareas.pop(eliminar - 1)
                return
                
def MostrarTareas():                
    print(" "  * 13,"📌 TAREAS 📌"," " * 15)
    print("-" * 40)
    print(" ID  |        TAREAS           | ESTADO ")
    print("-" * 40)
    for id, t in enumerate(tareas):
        
        print(f"📌 {id + 1}) {t['tarea']}  {'✅' if t['estado']==True else '⏳'}")
    print("-" * 40)


def main():
    while True:
        clear()
        print()
        print(" " * 8,"ADMINISTRADOR DE TAREAS", " " * 8)
        print()

        MostrarTareas()

        print()
        print("-" * 40)
        print("1) 📝 Agregar Tareas")
        print("2) ✅ Marcar como completada")
        print("3) 🗑️  Eliminar Tarea")
        print()
        print("0) 🚪 Salir")
        print("-" * 40)
    
        try:
            opt = int(input("Opcion: "))
        except ValueError:
            print("OPCION NO VALIDA. ⚠️")
            input()
            continue
        
        if opt in (1, 2, 3, 0):
            if opt == 1:
                AgregarTarea()
            elif opt == 2:
                MarcarTarea()
            elif opt == 3:
                EliminarTarea()
            elif opt == 0:
                GuardarJson(tareas)
                break
        else:
            print("OPCION NO ENCONTRADA. ⚠️")
            input()


main()
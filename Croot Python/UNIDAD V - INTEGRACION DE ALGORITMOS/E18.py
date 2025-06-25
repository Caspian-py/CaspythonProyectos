"""
    **Encuesta de edades y clasificación por rangos etarios.**
    | Rango | Edades             | Nombre del grupo |
    | ----- | ------------------ | ---------------- |
    | 0-12  | `0 <= edad <= 12`  | Niñez            |
    | 13-17 | `13 <= edad <= 17` | Adolescencia     |
    | 18-29 | `18 <= edad <= 29` | Juventud         |
    | 30-59 | `30 <= edad <= 59` | Adultez          |
    | 60+   | `edad >= 60`       | Vejez            |

"""
import os

edades = {
        "niñez": 0,
        "adolescencia": 0,
        "juventud": 0,
        "adultez": 0,
        "vejez": 0
    }

def mostrar():
    print("RANGOS ETARIOS")
    print("=" * 40)
    print(f"Niñez (0 - 12): {edades['niñez']}")
    print(f"Adolescencia (13 - 17): {edades['adolescencia']}")
    print(f"Juventud (18 - 29): {edades['juventud']}")
    print(f"Adultez (30 - 59): {edades['adultez']}")
    print(f"Vejez (60+): {edades["vejez"]}")
    print("=" * 40)


def contar():
    while True:
        os.system("cls")
        mostrar()
        print("Digite 'salir' para Salir.")
        opt = input("EDAD: ").strip()
        if opt.lower() == "salir":
            break
        
        if opt.isdigit():
            edad = int(opt)
            if edad >= 0 and edad <= 100:
                if edad >= 0 and edad <= 12:
                    edades['niñez'] += 1
                elif edad >= 13 and edad <= 17:
                    edades['adolescencia'] += 1
                elif edad >= 18 and edad <= 29:
                    edades['juventud'] += 1
                elif edad >= 30 and edad <= 59:
                    edades['adultez'] += 1
                elif edad >= 60:
                    edades['vejez'] += 1
            else:
                print("Edad no Valida.")
                input()
        elif not opt.isdigit():
            print("Edad no valida.")
            input()


contar()
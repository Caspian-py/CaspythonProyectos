"""
    Determinar la edad de una persona a partir de su anio de nacimiento.
"""
from datetime import datetime

an = int(input("Su anio de nacimiento fue: "))
aa = int(datetime.now().year)
edad = aa - an
print(f"Si naciste en el anio {an} y este anio es {aa} tu edad seria: {edad} anios.")
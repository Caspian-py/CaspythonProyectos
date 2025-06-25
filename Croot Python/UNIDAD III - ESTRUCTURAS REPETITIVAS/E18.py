"""
    **Leer N sueldos y mostrar cuántos están por encima del promedio.**
 """

sueldos = int(input("Cantidad de sueldos: "))
listaSueldos = []
ss = 0
for id in range(sueldos):
    sueldo = float(input(f"Sueldo ({id + 1}): "))
    ss += sueldo
    listaSueldos.append(sueldo)
sp = ss / sueldos
print()
print(f"Sueldo Promedio: ({sp})")
print()
msp = 0
for sueldo in listaSueldos:
    if sueldo >= sp:
        msp +=1

print(f"Cantidad de Sueldos Promedios: {msp}.")
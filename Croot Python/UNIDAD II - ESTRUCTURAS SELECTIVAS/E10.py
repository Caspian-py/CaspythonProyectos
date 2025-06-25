"""
    **Comparar tres números y decir cuál es el mayor.**
"""

n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))
n3 = float(input("Numero 3: "))
print()

if n1 > n2 and n1 > n3 :
    print(f"{n1} es el numero mayor.")
elif n2 > n3:
    print(f"{n2} es el numero mayor.")
else:
    print(f"{n3} es el numero mayor.")


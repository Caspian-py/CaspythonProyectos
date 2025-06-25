"""
    **Imprimir los primeros N términos de la serie Fibonacci.**
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

n = int(input("Valor N: "))
fib = 0
b = 1
for id in range(n):
    print(fib, end=" ")
    siguiente = fib + b
    fib = b
    b = siguiente
    


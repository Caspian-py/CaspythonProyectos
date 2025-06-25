"""
    **Generar los múltiplos de 5, comenzando de 0 hasta el 100.**
"""
for id in range(100 + 1):
    if id % 5 == 0:
        print(id, end=" ")

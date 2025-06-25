"""
    **Determinar si una letra es vocal o consonante.**
"""

letra = str(input("Letra: ").lower())


vocales = {"a", "e", "i", "o", "u"}

if letra in vocales:
    print(f"La letra {letra} es vocal.")
else:
    print(f"La letra {letra} es consonante.")

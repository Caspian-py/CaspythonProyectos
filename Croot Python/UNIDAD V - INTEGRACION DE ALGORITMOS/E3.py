"""
    **Encuesta de satisfacción:**
    Procesar respuestas de 100 personas (escala de 1 a 5).

    * Calcular porcentaje de cada opción.
    * Determinar la media y moda.
"""
import random
from collections import Counter
respuestas = [random.randint(1,5) for _ in range(2750)]

frecuencias = Counter(respuestas)
print("Frecuencias de cada opcion: ")
for opcion in range(1, 6):
    print(f"{opcion}: {frecuencias[opcion]} votos.")

print("Porcentaje por opcion: ")
for opcion in range(1, 6):
    cantidad = frecuencias[opcion]
    porcentaje = (cantidad / len(respuestas)) * 100
    print(f"Opsion {opcion}: {porcentaje:.2f}%")

media = sum(respuestas) / len(respuestas)

print(f"\nMedia de Satisfaccion: {media:.2f}")


moda = frecuencias.most_common(1)[0][0]
print(f"\nModa de Satisfaccion: {moda}")




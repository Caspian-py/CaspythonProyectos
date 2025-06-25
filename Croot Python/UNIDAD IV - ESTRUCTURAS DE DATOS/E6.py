"""
    **Leer dos vectores de 5 elementos y sumarlos elemento a elemento.**
"""
nums1 = []
nums2 = []
sum = []

print("VECTOR 1")
for id in range(5):
    value = float(input(f"Numero ({id + 1}): "))
    nums1.append(value)

print()
print("VECTOR 2")
for id in range(5):
    value = float(input(f"Nuumero ({id + 1}): "))
    nums2.append(value)

print()
print("SUMA VECTOR 1 Y VECTOR 2")
for id in range(5):
    value = nums1[id] + nums2[id]
    sum.append(value)
for value in sum:
    print(value, end=" ")

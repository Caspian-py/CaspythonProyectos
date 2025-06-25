"""
    Precio final de un artículo con 20% de descuento y 18%  de IGV**
    Mostrar el precio con descuento y el precio final.
"""

print("USUARIO VAMOS A CALCULAR EL PRECIO FINAL DE TU ARTICULO.")

nameArt = input("Nombre del Articulo: ")
precioArt = float(input(f"Precion del {nameArt}: "))

pt20 = precioArt - (precioArt * 0.20)
pt = pt20 + (pt20 * 0.18)

print(f"Estimado usuario, el precio de tu articulo({nameArt}) es de {precioArt} soles, con un descuento del 20% es {pt20} y con el IGV es {pt} soles, asi que vas a pagar a caja {pt} soles. GRACIAS POR TU COMPRAq!!")
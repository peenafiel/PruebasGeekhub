precio = 3.49
descuento = 0.4 # Es decir, se descuenta un 60% del total.
precio_descontado = precio * descuento

barras = input ("Introduzca las barras de pan que no son del día: ")
barras = int(barras)
print()
print("El precio habitual de las barras es de: " + str(precio) + "€")
print("El precio descontado es de: " + str(precio_descontado))
print("El coste final equivale a " + str(barras * precio_descontado))
edad = input('Introduce tu edad: ')
edad = int(edad)

if edad < 4:
    print("La entrada es gratuita.")
elif edad >= 4 and edad <= 18:
    print('El precio de la entrada es de 5€.')
else:
    print('El precio de la entrada es de 10€.')
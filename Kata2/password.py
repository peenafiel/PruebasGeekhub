password = "contraseña"

password_usuario = input("Introduzca la contraseña: ")
password_usuario = password_usuario.lower() # Para que así no distinga mayúsculas de minúsculas

if password == password_usuario:
    print("La contraseña es correcta")
else:
    print('La contraseña es incorrecta')
def Login(usuario, contrasena, intentos):
    if usuario == "usuario1" and contrasena == "asdasd":
        return True, intentos
    else:
        return False, intentos + 1

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    print(f"Intento {intentos + 1} de {max_intentos}")
    usuario = input("Introduce el nombre de usuario: ")
    contrasena = input("Introduce la cantraseña: ")

    exito, intentos = Login(usuario, contrasena, intentos)

    if exito:
        print("¡LOGIN CORRECTO! Bienvenido." )
        break
else:
    print("Has agotado los 3 intentos. Acceso denegao.")
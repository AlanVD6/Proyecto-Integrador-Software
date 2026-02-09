

usuario_correcto = "admin"
contrasena_correcta = "1234"
intentos_maximos = 3
intentos = 0
acceso_concedido = False

print("=== SISTEMA DE LOGIN SIMULADO ===\n")

while intentos < intentos_maximos and not acceso_concedido:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        acceso_concedido = True
        print("\n¡Acceso concedido! Bienvenido al sistema.")
    else:
        intentos += 1
        print("\nCredenciales incorrectas.")
        print("Intentos restantes:", intentos_maximos - intentos, "\n")

if not acceso_concedido:
    print("Demasiados intentos fallidos. Sistema bloqueado.")

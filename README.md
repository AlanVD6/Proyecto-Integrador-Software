Equipo 4 
Integrantes:
-Velazquez Diaz Alan
-Sarmiento Almanza Carlos Emilio
-Abella Henandez Marlon david
-Almanza Romo Alejandro


Este proyecto consiste en el desarrollo de un sistema de autenticación (Login) programado en Python.
El objetivo principal es simular el funcionamiento básico de un sistema de acceso que valide credenciales de usuario y limite la cantidad de intentos permitidos.

El sistema solicita un nombre de usuario y una contraseña, verificando si coinciden con las credenciales previamente definidas en el programa. En caso de ingresar datos incorrectos, el sistema informa al usuario y reduce el número de intentos disponibles. Si se excede el número máximo de intentos, el acceso es bloqueado.

Este proyecto permite aplicar conceptos fundamentales de programación como:

Variables
Condicionales
Ciclos (while)
Control de flujo
Validación de datos
Uso de Git y GitHub para control de versiones

Tecnologías Utilizadas

Python 3
Git
GitHub
Visual Studio Code

1. Instrucciones de Ejecución
git clone https://github.com/AlanVD6/Proyecto-Integrador-Software.git
2. Ingresar a la carpeta del proyecto:
cd Proyecto-Integrador-Software
3. python login.py
4. Ingresar las credenciales solicitadas en la consola.

Funcionamiento del Sistema
El sistema permite un máximo de 3 intentos.
Usuario correcto: admin
Contraseña correcta: 1234
Si las credenciales son correctas - se concede el acceso.
Si son incorrectas - se descuenta un intento.
Después de 3 intentos fallidos - el sistema se bloquea.

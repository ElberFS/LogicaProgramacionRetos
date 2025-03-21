# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
#  * creando una que sea capaz de encontrar y extraer todos los números
#  * de un texto.
#  *


import re

texto1 = "Hoy 21 de marzo es viernes del mes 3, y quiero jugar 3 pártidas de aram aña 5"

condicion = r"\d+"

numeros =re.findall(condicion,texto1)

print(numeros)

#  * DIFICULTAD EXTRA (opcional):
#  * Crea 3 expresiones regulares (a tu criterio) capaces de:
#  * - Validar un email.
#  * - Validar un número de teléfono.
#  * - Validar una url.
#  */


validar_email = r"^[0-9A-Za-z_.-]+@[0-9A-Za-z-]+\.[0-9A-Za-z.]+$"

email = "marts.capricornio@gmail.com.34"

respusta=re.match(validar_email,email)
print(f"{email}: {'Correo valido'  if respusta else 'Email No valido'}")

validar_numero = r"^9[0-9]{8}$"

numero = "102329"
respuesta2 = re.match(validar_numero,numero)
print(f"{numero}: {'Numero valido' if respuesta2 else 'Numero No valido'}")

validar_url = r"^https://[A-Za-z0-9.-]+\.[A-Za-z]{2,6}(/.*)?$"


url = "https://jkanime.net/"

respuesta3 = re.match(validar_url,url)
print(f"{url}: {'URL valido' if respuesta3 else 'URL No valido'}")

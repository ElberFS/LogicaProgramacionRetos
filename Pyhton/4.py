# /*
#  * EJERCICIO:
#  * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
#  * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
#  * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
#  *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
#  *



cadena1 = "Hola"
cadena2 = "como estas?"

#1.longitud
print(len(cadena1))

#2.concatenacion
print(cadena1+" "+cadena2)

#3.concatenacion con f string
print(f"{cadena1} {cadena2}")

#4.acceso a caracteres especificos
print(cadena1[2]) #a un caracter
print(cadena1[0]) # al primer caracter
print(cadena1[-1]) # al ultimo caracter

#4.subcadenas
print(cadena2[0:4])
print(cadena2[5:])

#4.subacenas con saltos
print(cadena2[0:11:2]) # significa que tome desde el caracter 0 hasta el 11 y vaya de 2 en 2
print(cadena2[0::2]) # en caso no quieras tomar toda la cadena puedes puedes dejar solo ::
print(cadena2[::-1]) # invertir cadena

#5.repeticion
print(cadena1 *3)

#6. recorrido

for c in cadena2 :
    print(c)

#6.Convertir minusculas a mayusculas
print(cadena1.upper())

#7.Convertir mayusculas a minusculas
print(cadena1.lower())

print(cadena2.capitalize()) #para que la primra letra fuera mayuscula
print(cadena2.title()) #para que sea un titulo

#8. Remplazo
print(cadena2.replace("estas", "pastel"))

#9. divison
print(cadena2.split(" "))

#10. union de cadenas
print("-".join([cadena2, cadena1])) # con varias cadenas
print("-".join(cadena2)) # con una sola cadena, toma a la cadena como si fuera una lista y uno lo caracteres


#11. interpolacion

#forma moderna y actual
lenguaje = "Python"
disciplina = "Ciencia de datos"
print(f"{lenguaje} es el mejor lenguaje del mundo, con el puedes trabajar en {disciplina}")


#forma algo antigua
print("{} es el mejor lenguaje del mundo, con el puedes trabajar en {}".format(lenguaje,disciplina))

#hay mas formas pero esas ya son arcaicas, si quieres buscale :v

#12. verificar
print(cadena1.startswith("Ho")) #empieza con
print(cadena2.endswith("?")) #termina con 
print("como" in cadena2) #verificar si existe algo en la cadena      
print(cadena2.isalpha()) #verificar si tiene caracteres lfanumericos

#13. Eliminar espacios vacios
print(cadena2.strip())
print(cadena2.rstrip())
print(cadena2.lstrip())

#14. encontrar la posicion de una subcadena
print(cadena2.find("estas"))

#15.ocurrencias
#cuantas veces se repite un caracter
print(cadena2.count("o"))


# * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
#  * para descubrir si son:
#  * - Palíndromos
#  * - Anagramas
#  * - Isogramas
#  */

def palindromos(texto1, texto2):
    texto1 = texto1.lower().replace(" ","")
    texto2 = texto2.lower().replace(" ","")

    if texto1 == texto1[::-1]:
        print(f"{texto1} es polindromo")
    else:
        print(f"{texto1} no es polindromo")

    if texto2 == texto2[::-1]:
        print(f"{texto2} es polindromo")
    else:
        print(f"{texto2} no es polindromo")

def anagramas(texto1, texto2):
    texto1 = texto1.lower().replace(" ","")
    texto2 = texto2.lower().replace(" ","")

    if sorted(texto1) == sorted(texto2) :
        print(f"{texto1} y {texto2} son anagramas")
    else:
        print("No son anagramas")


def isogramas(texto1, texto2):
    texto1 = texto1.lower().replace(" ","")
    texto2 = texto2.lower().replace(" ","")

    if len(texto1) == len(set(texto1)):
        print(f"{texto1} es un isograma")
    else:
        print(f"{texto1} no es un isograma")

    if len(texto2) == len(set(texto2)):
        print(f"{texto2} es un isograma")
    else:
        print(f"{texto2} no es un isograma")


palindromos("arenera","reconocer")
anagramas("perro","repro")
isogramas("murcielago","casa")
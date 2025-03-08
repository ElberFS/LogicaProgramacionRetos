# EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.


#funcion basica:
def Saludar():
    print("Hola")

Saludar()

#con parametros:

def Suma(a,b):
    resultado = a+b
    print(f"resultado es : {resultado}")

Suma(23,16)

#con retorno

def Suma(a,b):
    resultado = a+b
    return resultado

suma_total = Suma(23,16)

print(f"resultado es : {suma_total}")

#con varios parametros
def Suma_Numeros(*numeros):
    return sum(numeros)

resultado = Suma_Numeros(10,23,19.3,7,9,11,2)

print(f"resultado es : {resultado}")


#otra forma de usar varios parametros
lista = [10,23,19.3,7,9,11,2]

def Suma_Numeros(numeros):
    return sum(numeros)

resultado = Suma_Numeros(lista)

print(f"resultado es : {resultado}")


#funcion dentro de otra funcion

def funcion1():
    print("Hola primera funcion")

    def funcion2():
        print("Hola segunda funcion, estas adentro de funcion 1")

    funcion2()

funcion1()

#variables globales y locales

Lista_global = [12, 200, 5, 1.59] #global , fuera de una funcion normalemente al principio de un codigo

def suma_global(numeros):
    return sum(numeros)

def suma_local():
    lista_local = [90,29,18] #local , esta en una funcion
    return sum(lista_local)

resultado1 = suma_global(Lista_global)
resultado2 = suma_local()

print(f"resultado1 es : {resultado1}")
print(f"resultado2 es : {resultado2}")


#DIFICULTAD EXTRA
def reto2(texto1,texto2):
    total = 0
    for elemento in range(1,101):
        if elemento%3 == 0 and elemento%5==0:
            print(f"{texto1} {texto2}")
        elif elemento%3==0:
            print(f"{texto1}")
        elif elemento%5==0:
            print(f"{texto2}")
        else:
            total +=1
            print(f"{elemento}")
        
    return total
    

cadena1 = input("Escribe la primera cadena: ")
cadena2 = input("Escribe la segunda cadena: ")

total_numeros = reto2(cadena1,cadena2)
print(f"Total de numeros en lugar de cadenas: {total_numeros}")



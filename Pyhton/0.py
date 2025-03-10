#EJERCICIO:
#  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
#  *   lenguaje de programación que has seleccionado.
#  * - Representa las diferentes sintaxis que existen de crear comentarios
#  *   en el lenguaje (en una línea, varias...).
#  * - Crea una variable (y una constante si el lenguaje lo soporta).
#  * - Crea variables representando todos los tipos de datos primitivos
#  *   del lenguaje (cadenas de texto, enteros, booleanos...).
#  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


#https://www.python.org/

#comentario de una linea

"""
comentario en 
varias 
lineas 
con comillas

"""

'''
comentario en 
varias lineas 
con comillas
siples aña
'''

#creacion de variables

entero = 24
flotante = 12.9
cadena = "Hola aña"
boleano = True #puede ser tambien false
lista =[] #lista vacia
lista2 = [12,23,10,"Hola", True,[10,23.9,1],"Quiroz Kabro :v"]

dicionario = {} #diccionario vacio
dicionario2 = {
                'Nombre' : 'Martin de Jesús',
                'Apellidos': 'Lozano Silvestre',
                'Edad': 23,
                'Ciudad': 'Lambayeque',
                'situacion Laboral': 'No hay chamba :v'
              }

tuplas = () #tupla vacia
tuplas2 = (12,90,17.2,True,"Chiclayostan")

conjuntos = {} #parece un diccionario pero no lo es uwu(el conjunto tambien se le llama set)

conjuntos2 = {1,2,3,8,10,20,True}

#en python no existen las constantes, pero una manera de representarlas es escribiendo en mayusculas
PI = 3.14
IGV = 0.18
NOM_UNIVERSIDAD = "Pedro Ruiz Gallo"


nombre_lenguaje = input("Ingresa nombre de lenguaje: ")
print(f"¡Hola, {nombre_lenguaje}")
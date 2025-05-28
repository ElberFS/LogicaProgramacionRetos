# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
#  * operaciones (debes utilizar una estructura que las soporte):
#  * - Añade un elemento al final.
#  * - Añade un elemento al principio.
#  * - Añade varios elementos en bloque al final.
#  * - Añade varios elementos en bloque en una posición concreta.
#  * - Elimina un elemento en una posición concreta.
#  * - Actualiza el valor de un elemento en una posición concreta.
#  * - Comprueba si un elemento está en un conjunto.
#  * - Elimina todo el contenido del conjunto.
#  *

conjunto = {"hola",1,24.1,True,12,2}

#el orden en los conjuntos no existe por lo que solo se agrega el valor en el conjunto, no exite un principio ni final
conjunto.add(45)
print(conjunto)

'''
en este caso se utilizara la lista como un conjunto de datos
'''

lista1 = ["hola",1,24.1,True,12,2]
#agregando al final
lista1.append(34)
print(lista1)

#agregando al principio
lista1.insert(0,90)
print(lista1)

#agregando en bloque al final
lista1.extend([31,76,91,65])
print(lista1)

#agregando en bloque al principio
lista1[:0] = ["Juan","Peru"]
print(lista1)

#agregando en bloque en posicion especifica
lista1[3:3] = [69,False,"remplazo"]
print(lista1)

#eliminando una posicion en concreto
del lista1[5]
print(lista1)

#actualiza el valor en una posicion
lista1[6] = "gaaaa"
print(lista1)

#buscar si existe en la lista un elemento
respuesta = 11 in lista1
print(f"Respuesta : {respuesta}")

#elimino todo el contenido
lista1.clear()
print(lista1)

print("---------------------------------------------")
#  * DIFICULTAD EXTRA (opcional):
#  * Muestra ejemplos de las siguientes operaciones con conjuntos:
#  * - Unión.
#  * - Intersección.
#  * - Diferencia.
#  * - Diferencia simétrica.
#  */

conjunto_a = {1,2,3,5,8}
conjunto_b = {5,6,7,8}

#UNION
union =  conjunto_a | conjunto_b
print(union)

#otra forma de union
print(conjunto_b.union(conjunto_a))


#INTERSECCION
interseccion = conjunto_a & conjunto_b
print(interseccion)

#otra forma
print(conjunto_a.intersection(conjunto_b))

#DIFERENCIA

diferencia_a = conjunto_a - conjunto_b
print(diferencia_a)

diferencia_b = conjunto_b -conjunto_a
print(diferencia_b)

#otra forma

print(conjunto_a.difference(conjunto_b))

print(conjunto_b.difference(conjunto_a))


#DIFERENCIA SIMETRICA
diferencia_simetrica = conjunto_a ^ conjunto_b
print(diferencia_simetrica)

#otra forma
print(conjunto_a.symmetric_difference(conjunto_b))
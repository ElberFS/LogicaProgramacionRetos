# EJERCICIO:
#  * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
#  *   su tipo de dato.
#  * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
#  *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
#  * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)


#variables por valor : esto aplica para int , float , booleanos , strings y tuplas
a = 10
b=a #copia el valor de a en b

print(a) #ambos valen 10
print(b)
b= 69 # se le cambia el valor a b, pero a no cambia

print(a) # a = 10
print(b) #b = 69


#variables por referencia: aplica tambien para diccionarios y sets
lista1 = [10,29,19.9 ,11]
lista2 = lista1
print(lista1)
print(lista2)

lista2.append(60)

print(lista1)
print(lista2)


#funciones con asignacion por valor
entero = 20
def por_valor(numero):
    numero=11
    print(numero)

por_valor(20)
print(entero)


#funciones con asignacion por referencia
lista_num = [10,11,28,0.2,4.5,12,988]
def por_referencia(lista):
    lista.append(55)
    print(lista)

por_referencia(lista_num)
print(lista_num)


#  DIFICULTAD EXTRA (opcional):
#  * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
#  * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
#  *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
#  *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
#  *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
#  *   Comprueba también que se ha conservado el valor original en las primeras.
#  */

def programa_por_valor(valor1, valor2):
    valor1,valor2 = valor2,valor1

    return valor1, valor2

def programa_por_referencia(valor1,valor2):

    valor1[:], valor2[:] = valor2[:], valor1[:]
    return valor1,valor2


v1 = 30
v2 = 20
numero1, numero2 = programa_por_valor(v1,v2)

print("POR VALOR")
print(f"Valores antes del intercambio: {v1} {v2}")

print(f"Valores despues del intercambio: {numero1} {numero2}")


l1 = [80,79,"Hola"]
l2 = [190,9,True]

print("POR REFERENCIA")
print(f"Valores antes del intercambio: {l1},{l2}")
lista_r1 , lista_r2 = programa_por_referencia(l1,l2)


print(f"Valores despues del intercambio: {lista_r1} {lista_r2}")


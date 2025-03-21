# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
#  * números del 1 al 10 mediante iteración.
#  *


#1. usando for:
print("USANDO FOR")
for numero in range(1,11):
    print(numero)

#2. usando while
print("USANDO WHILE")
numero = 1
while numero <11:
    print(numero)
    numero += 1

#4.usando listas:
print("USANDO LISTA")
lista = [1,2,3,4,5,6,7,8,9,10]
for num in lista:
    print(num)


#  * DIFICULTAD EXTRA (opcional):
#  * Escribe el mayor número de mecanismos que posea tu lenguaje
#  * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
#  */

#1 con range
for num in range(5):
    print(num)

#2 con while
num = 0
while num < 5:
    print(num)
    num += 1

#3.con listas
ciduades = ["Lima", "Lambayeque", "Arequipa","Cuzco","Ica"]
for ciudad in ciduades:
    print(ciudad)


#4.con diccionario
precios = {"limon": 3.20, "uva": 5, "mango": 3}
for fruta, precio in precios.items():
    print(f"{fruta}: S/.{precio}")


#5.con conjunto
colores = {"rojo", "verde", "azul","amarillo","ocre"}
for color in colores:
    print(color)


#6.con enumerate
ciduades = ["Lima", "Lambayeque", "Arequipa","Cuzco","Ica"]
for i,ciudad in enumerate(ciduades,1):
    print(f"{i}. {ciudad}")


#7. con zip()
nombres = ["Paco", "Roberto", "Elber"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")


#8. con comprension de listas 
doble = [x*2 for x in range(1,6)]
print(doble)


#9.con map()
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)

#10 con recursion

def conteo(numero):
    if numero==0:
        print(numero)
    else:
        print(numero)
        conteo(numero-1)

conteo(10)
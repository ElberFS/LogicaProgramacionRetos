# EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


a = 9
b= 5

#suma

print(f'{a+b}')

#resta
print(f'{a-b}')

#multiplicacion
print(f'{a*b}')

#potenciacion
print(f'{a**b}')

#division
print(f'{a/b}')

#division entera (devuelve la parte entera sin decimales)
print(f'{a//b}')

#modulo (devuelve el residuo)
print(f'{a%b}')

#asginacion se hace desde el principio que seria el =
#a=b
print(f'{a}')

#asignacion con suma
#a+=b #seria a= a+b
print(f'{a}')

#asignacion con suma
#a-=b #seria a= a-b
print(f'{a}')

'''
lo mismo seria para multiplicacion potenciacion todos con 
su respectivo signo y el = , *=, //= , /= , **=, %=

'''


#desplazamiento a la izquierda
print(f'{a<<b}')

#desplazamiento a la derecha
print(f'{a>>b}')

#comparacion
print(f'{a>b}')

print(f'{a<b}')

print(f'{a==b}')

print(f'{a>=b}')

print(f'{a<=b}')

print(f'{a!=b}')

#Logicos

print(f'{True and True}')
print(f'{True and False}')


print(f'{True or True}')
print(f'{True or False}')

print(f'{not True}')
print(f'{not False}')

#Luego hay otros operadores mas que son bitwise, pero busquelo usted, no sea mamon :v



#estructuras de datos

#if
if a>b :
    print("Ta bien aña")
else:
    print("Ta mal uwu")

#elif

if a!=b :
    print(f"{a} Diferente de {b}")
elif a<b:
    print(f"{a} Es menor de {b}")
else:
    print("Ya mucho : v")


#while
while a>=b:
    b+=1
    if b<=a :
        print("Sigue siendo mayor")
    else:
        print("Ya no es mayor uwu")


#for
#para usos del for necesito crear una lista, aunque no siempre es necesario

lista = [a,b]

for elemento in lista:
    print(f'{elemento} de la lista')

'''
Existen mas usos para el for como el continue que sirve para saltar la iteracion y pasar a la siguiente
y break para terminar la iteracion.
'''

#ejercicio de dificultad extra

for elemento in range(10,56):
    if elemento == 10 or elemento==55:
        print(f'{elemento}')
    elif elemento == 16:
        continue
    elif elemento%3 == 0:
        continue
    else:
        print(f'{elemento}')
        
        
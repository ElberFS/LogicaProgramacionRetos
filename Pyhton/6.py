# /*
#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.


def recursivo(n):
    if n == 0:
        print(n)
        return
    
    print(n)
    recursivo(n-1)
    
recursivo(100)


#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).
#  */

#factorial
def factorial(n):
    if n==0:
        return 1
    return n* factorial(n-1)

print(factorial(5))

#serie de fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
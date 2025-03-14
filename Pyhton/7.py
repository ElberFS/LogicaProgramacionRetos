# /*
#  * EJERCICIO:
#  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
#  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
#  * o lista (dependiendo de las posibilidades de tu lenguaje).
#  *

from collections import deque

#PILAS : primero en entrar ultimo en salir(LIFO = last in, first out)
pila1 = [12,45,11,2.3]

#agregando elementos
pila1.append(56)
pila1.append(1.29)
print(pila1)

#elimimando elemento siempre por el ultimo(esto se puede considerar com una extraccion)

elemento = pila1.pop()
print(elemento)
print(pila1)

#para ver el siguiente elemento en la pila que sigue
siguiente = pila1[-1]
print(siguiente)

#COLAS : primero en entrar primero en salir (FIFO = first in, first out)
cola = deque(["Hola",True,1.20,87])

#agregando
cola.append(60)
print(cola)

#extrayendo o eliminando
elemento2 = cola.popleft()
print(elemento2)
print(cola)

#para ver el siguiente elemento que sigue en la cola
siguiente2 = cola[0]
print(siguiente2)


#  * DIFICULTAD EXTRA (opcional):
#  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#  *   el nombre de una nueva web.


paginas_adelante = ["Inicio"]
paginas_atras =[]


def adelante():
    
    if len(paginas_atras)> 0:
        pag_adelante = paginas_atras.pop()
        paginas_adelante.append(pag_adelante)
    else:
        print("Ya no hay mas paginas adelante")

def atras():

    if len(paginas_adelante) > 1:
        pag_atras=paginas_adelante.pop()
        paginas_atras.append(pag_atras)
    else:
        print("Ya no existen mas paginas")


def agregar_pagina():
    if len(paginas_atras) > 0:
        paginas_atras.clear()

    nueva_pagina = input("Nueva pagina: ")
    paginas_adelante.append(nueva_pagina)


def navegacion():
        print("LA WEB")
        print(f"--Pagina actual: {paginas_adelante[-1]}")
        print("(+)    Nueva pagina a visitar")
        print("(<-)  Atras")
        print("(->)  Adelante")
        print("(esc)  salir")
    

def main1():
    while True:
        navegacion()

        opcion = input("Seleccione: ")
        
        if opcion == "+":
            agregar_pagina()
        elif opcion == "<-":
            atras()
        elif opcion == "->":
            adelante()
        elif opcion == "esc":
            print("Saliendo")
            break
        else:
            print("Opcion invalida")

main1()



#  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#  *   interpretan como nombres de documentos.
#  */

documentos = deque()

def agregar_documento():
    doc = input("ingrese documento : ")
    documentos.append(doc)

def imprimir_documento():
    if len(documentos) > 0:
        doc_impreso = documentos.popleft()
        print(f"Documento impreso: {doc_impreso}")
    else:
        print("No hay documentos en cola")


def menu():
    if len(documentos) > 0:
        print("IMPRESORA")
        print(f"Siguiente documento: [{documentos[0]}]")
        print("(+)  Agregar documento a imprimir")
        print("(1)  Imprimir")
        print("(2)  Salir")
    else:
        print("IMPRESORA")
        print(f"Siguiente documento: [En espera]")
        print("(+)  Agregar documento a imprimir")
        print("(1)  Imprimir")
        print("(2)  Salir")


def main2():
    while True:
        menu()

        opcion = input("Seleccione: ")
        
        if opcion == "+":
            agregar_documento()
        elif opcion == "1":
            imprimir_documento()
        elif opcion == "2":
            print("Saliendo")
            break
        else:
            print("Opcion invalida")


main2()
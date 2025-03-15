# /*
#  * EJERCICIO:
#  * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#  * atributos y una función que los imprima (teniendo en cuenta las posibilidades
#  * de tu lenguaje).
#  * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#  * utilizando su función.

from collections import deque

#CREANDO UNA CLASE:

#creando clase con atributos
class Alumno:
    Nombre = "Martín de Jesús"
    Edad = 23
    Direccion = "Junin 569"

    def __init__(self,argumento1):
        print("inicializando alumno")
        self.argumento1 = argumento1

objeto_alumno = Alumno("hola como estan")


#inicializador

'''
En la mayoría de los casos, cuando la gente habla de un "constructor" 
en Python, realmente se refieren a __init__, aunque técnicamente __new__ 
es el verdadero constructor.
'''

class Persona:
    correo = "marts@gmail.com"
    direccion = "bacamatos 325"

    def  __init__(self,nombre,apellido,edad):
        print("Inicializando persona")
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #creando un metodo
    def imprimir_datos(self):
        #forma no optima en caso sean muchos datos
        # print("Datos del objeto:")
        # print(f"Nombre : {self.nombre}")
        # print(f"Apellido : {self.apellido}")
        # print(f"Edad : {self.edad}")

        for key,value in self.__dict__.items():
            print(f"{key} : {value}")


#instancia creada
objeto_persona = Persona("Juan","Añanay",56)

#mostrar valores
objeto_persona.imprimir_datos()

#modificar atributos
objeto_persona.nombre= "Karlo"
objeto_persona.edad= "34"

objeto_persona.imprimir_datos()


#  * DIFICULTAD EXTRA (opcional):
#  * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#  * en el ejercicio número 7 de la ruta de estudio)
#  * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#  *   retornar el número de elementos e imprimir todo su contenido.
#  * 
#  */



class Pila:
    def __init__(self):
        self.lista = []
    
    def insertar(self,valor):
        self.lista.append(valor)

    def eliminar(self):
        eliminado = self.lista.pop()
        print(f"Elemento eliminado: {eliminado}")

    def cantidad(self):
        print(f"Cantidad de elementos: {len(self.lista)}")

    def imprimir(self):
        print(self.lista)

#inicializar
mi_pila = Pila()

#agregar elementos
mi_pila.insertar(39)
mi_pila.insertar("Gaaa")
mi_pila.insertar(True)
mi_pila.insertar(10.997)

#mostrar elementos
mi_pila.imprimir()

#eliminar
mi_pila.eliminar()
mi_pila.imprimir()

#cantidad de elementos:
mi_pila.cantidad()


class Cola:
    def __init__(self):
        self.lista = deque()
    
    def insertar(self,valor):
        self.lista.append(valor)

    def eliminar(self):
        eliminado = self.lista.popleft()
        print(f"Elemento eliminado: {eliminado}")

    def cantidad(self):
        print(f"Cantidad de elementos: {len(self.lista)}")

    def imprimir(self):
        print(self.lista)

#inicializar
mi_cola = Cola()

#agregar elementos
mi_cola.insertar(39)
mi_cola.insertar("Gaaa")
mi_cola.insertar(True)
mi_cola.insertar(10.997)

#mostrar elementos
mi_cola.imprimir()

#eliminar
mi_cola.eliminar()
mi_cola.imprimir()

#cantidad de elementos:
mi_cola.cantidad()
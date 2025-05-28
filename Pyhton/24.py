# /*
#  * EJERCICIO:
#  * Explora el concepto de "decorador" y muestra cómo crearlo
#  * con un ejemplo genérico.

#USO DE UN DECORADOR CON PARAMETRO, FUNCIONA IGUAL COMO SI NO TUVIERA PARAMETROS
def Decorador1(func):

    def SaludarDecorado(cadena):
        print("Empezando conversacion")
        func(cadena)
        print("Adios, finalizando conversacion")
    
    return SaludarDecorado


@Decorador1
def Saludar(nombre):
    print(f"Hola que tal {nombre}, gaaaaaaaaaaaaaaaaaaa")

Saludar("Martin")


#USO DE VARIOS ARGUMENTOS
#lista1 = [23,11,5,7.8,1]

def Decorador2(func):
    def sumar_decorado(*args):
        print("Ejecutando....")
        func(*args)
        print("finalizando ejecucion")

    return sumar_decorado


@Decorador2
def sumar(a,b,c,d):
    print(a+b+c+d)

sumar(11,34,4,9)

#DECORADORES PROPIOS DE PYTHON
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
    
    @property
    def mostrar_nombre(self):
        return self.nombre
    

obj_persona = Persona("Roberto")

print(obj_persona.mostrar_nombre)



#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un decorador que sea capaz de contabilizar cuántas veces
#  * se ha llamado a una función y aplícalo a una función de tu elección.
#  */


def Decorador3(func):

    def saludar_nombre_decorado(cadena):
        saludar_nombre_decorado.contador +=1
        print(f"La función '{func.__name__}' ha sido llamada {saludar_nombre_decorado.contador} veces")
        func(cadena)
    saludar_nombre_decorado.contador = 0
    return saludar_nombre_decorado


@Decorador3
def saludar_nombre(nombre):
    print(f"hola {nombre}")


saludar_nombre("Juan")
saludar_nombre("Paco")
saludar_nombre("Martin")
saludar_nombre("Giovani")




def Decorador4(func):
    def contar_desde_decorado(numero):
        contar_desde_decorado.contador += 1 
        print(f"Llamada numero: {contar_desde_decorado.contador}")
        func(numero)  # Llama a la función original
    contar_desde_decorado.contador = 0  # Inicializa el contador
    return contar_desde_decorado


@Decorador4
def contar_desde(numero):
    print(numero)
    if numero > 0:
        contar_desde(numero-1)

contar_desde(10)
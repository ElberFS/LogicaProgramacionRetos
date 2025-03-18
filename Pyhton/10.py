# /*
#  * EJERCICIO:
#  * Explora el concepto de manejo de excepciones según tu lenguaje.
#  * Fuerza un error en tu código, captura el error, imprime dicho error
#  * y evita que el programa se detenga de manera inesperada.
#  * Prueba a dividir "10/0" o acceder a un índice no existente
#  * de un listado para intentar provocar un error.


#EXCEPCIONES

# a = 10
# b= 0
# lista = [10,2,11,9,7.4]

# print(lista[9])

# #print(a/b)

# #1. primera de forma de controlar excepciones
# print("-----------------------------")
# if b!=0:
#     print(a/b)
# else:
#     print("Error: No se puede dividir entre 0")


# #2. segunda forma: usando raise para lanzar excepcion especifica
# print("-----------------------------")
# # if b!=0:
# #     print(a/b)
# # else:
# #     raise ZeroDivisionError("Error: No se puede dividir entre 0")


# #3. tercera forma: usando try except para que el programa no se detenga
# print("-----------------------------")
# try:
#     resultado = a/b
#     print(resultado)
# except ZeroDivisionError:
#     print("no se puede dividir entre 0")


# #puede tambien usarse el TypeError ,ValueError, 
# print("-----------------------------")
# try:
#     resultado = a/b
#     resultado2 = 4+ "Aña"
#     print(resultado)
# except ZeroDivisionError:
#     print("No se puede dividir entre 0")
# except TypeError:
#     print("Problema con tipo de datos")

# print("-----------------------------")
# try:
#     resultado = a/b
#     resultado2 = 4+ "Aña"
#     print(resultado)
# except (ZeroDivisionError, TypeError):
#     print("Excepcion ZeroDivision/TypeError")


# # tambien otra forma de usarlo sin nececidad de especificar
# #el tipo de excepcion

# print("-----------------------------")
# try:
#     resultado = 10/0
#     resultado2 = 42+ "Aña"
#     print(resultado)
# except Exception as e: #para saberel tipo de excepcion
#     print(f"Excepcion: {type(e)}") 



#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que sea capaz de procesar parámetros, pero que también
#  * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
#  * corresponderse con un tipo de excepción creada por nosotros de manera
#  * personalizada, y debe ser lanzada de manera manual) en caso de error.
#  * - Captura todas las excepciones desde el lugar donde llamas a la función.
#  * - Imprime el tipo de error.
#  * - Imprime si no se ha producido ningún error.
#  * - Imprime que la ejecución ha finalizado. 
#  */


#excepcion perzonalizada
class MiExcepcion(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje


def lanzar_excepcion(parametro1,parametro2):
    suma = parametro1+parametro2
    if not isinstance(parametro1 , int) or not isinstance(parametro2,int):
        raise TypeError("ambos parametros deben ser enteros")
    if suma <10 :
        raise ValueError("La suma debe ser mayor a 10")
    if suma == 69:
        raise MiExcepcion("La suma no puede ser 69")
    
    return f"Los valores: {parametro1} y {parametro2} son validos y se proceso correctamenta dando suma de {suma}"


try:
    resultado = lanzar_excepcion(11,58)
    print(resultado)
    print("No se ha producido ningun error")

except Exception as error:
    print(f"Error de tipo: {type(error).__name__} - {error}")

finally:
    print("La ejecucion ha finalizado")

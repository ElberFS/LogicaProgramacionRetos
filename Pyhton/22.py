# /*
#  * EJERCICIO:
#  * Explora el concepto de funciones de orden superior en tu lenguaje 
#  * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
#  *

'''
Una funcion de orden superior recibe otra funcion como argumento o devuelve 
una funcion, especialmente usadas en el paradigma funcional

mientras que un callbacks es aquella funcion que se pasa como parametro osea es la
que funciona como llamada
'''

from datetime import datetime

#RECIBE UNA FUNCION COMO ARGUMENTO
def Operaciones(operacion,numeros):
    return operacion(numeros)

def suma(numeros):
    print(sum(numeros))

def multiplicacion(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num

    print(resultado)

lista = [2,19.2,11,42,8]
Operaciones(multiplicacion,lista)

#DEVUELVE UNA FUNCION

def calculador(constante):
    def resultado(valor):
        return round(constante*valor,2)
    return resultado

calcular_igv = calculador(0.18)
descuento = calculador(0.35)
print(calcular_igv(280))
print(descuento(94))


#USO DE MAP

cuadrado = list(map(lambda x:x**2 , lista))
print(cuadrado)

#USO DE FILTER
pares = list(filter(lambda x:x %2 == 0, lista))
print(pares)


#  * DIFICULTAD EXTRA (opcional):
#  * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
#  * lista de calificaciones), utiliza funciones de orden superior para 
#  * realizar las siguientes operaciones de procesamiento y análisis:
#  * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
#  *   y promedio de sus calificaciones.
#  * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
#  *   que tienen calificaciones con un 9 o más de promedio.
#  * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
#  * - Mayor calificación: Obtiene la calificación más alta de entre todas las
#  *   de los alumnos.
#  * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
#  */


Estudiantes =[
    {"nombre":"Juan Paiva","fecha_nacimiento":"10-04-2000","calificaciones":[10,10.8,17,18,13]},
    {"nombre":"Roberto Diescanceso","fecha_nacimiento":"11-11-2001","calificaciones":[12,8,4,5.9,11]},
    {"nombre":"Giovani Jauregi","fecha_nacimiento":"23-09-2000","calificaciones":[15,14.7,17,19,16]},
    {"nombre":"Elber Guenzas","fecha_nacimiento":"15-07-2002","calificaciones":[15,16.5,17,14,15]}
]




def promedio():
    promedio_estudiantes = list(map(
        lambda e:{
            "nombre": e["nombre"],
            "promedio": sum(e["calificaciones"])/len(e["calificaciones"])
        },
        Estudiantes
    ))

    print("Promedio de estudiantes:")
    for estudiante in promedio_estudiantes:
        print(f"Estudiante : {estudiante["nombre"]} - Promedio: {estudiante["promedio"]}")

promedio()

def mejores():

    mejores_estudiante = list(map(
        lambda e : e["nombre"] , filter(
            lambda e: (sum(e["calificaciones"])/len(e["calificaciones"])) >= 9 ,
            Estudiantes
        )
    ))
    print("Mejores estudiante, promedio mayor o igual a 9")
    for estudiante in mejores_estudiante:
        print(f"Estudiante : {estudiante}")

mejores()

def nacimiento():
    orden_nacimiento = list(sorted(
        Estudiantes,
        key=lambda e: datetime.strptime(e["fecha_nacimiento"],"%d-%m-%Y"),
        reverse=True
    ))

    print("Estudiantes ordenados por fecha de nacimiento")
    estudiantes_orden = list(map(
        lambda e : e["nombre"], orden_nacimiento
    ))

    for estudiante in estudiantes_orden:
        print(f"- {estudiante}")

nacimiento()

def mayor_calificacion():
    calificaciones = max(map(
        lambda e : max(e["calificaciones"]), Estudiantes
    ))

    print(calificaciones)
    
mayor_calificacion()




# /*
#  * EJERCICIO:
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.
#  *

import asyncio
from datetime import datetime

async def funcion_asincronica(nombre,duracion):
    inicio=datetime.now().strftime("%H:%M:%S")
    print(f"funcion : {nombre} comenzo: {inicio} - duracion:{duracion} segundos")

    await asyncio.sleep(duracion)

    fin=datetime.now().strftime("%H:%M:%S")
    print(f"funcion: {nombre} finalizo: {fin}")


def funcion1():
    print("Hola soy la funcion 1")

def funcion2():
    print("Hola soy la funcion 2")



#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han
#  *   finalizado.
#  */

def funcion_A():
    print("funcionA")

def funcion_B():
    print("funcionB")

def funcion_C():
    print("funcionC")

def funcion_D():
    print("funcionD despues de ejecutarse todas")

async def tareas_paralelas():
    tareaC = asyncio.create_task(funcion_asincronica(funcion_C.__name__,3))
    tareaB = asyncio.create_task(funcion_asincronica(funcion_B.__name__,2))
    tareaA = asyncio.create_task(funcion_asincronica(funcion_A.__name__,1))
    await asyncio.gather(tareaC,tareaB,tareaA)

async def main():
    await tareas_paralelas()
    tareaD = asyncio.create_task(funcion_asincronica(funcion_D.__name__,1))
    await tareaD
    

asyncio.run(main())
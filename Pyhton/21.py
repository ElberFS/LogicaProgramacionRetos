# /*
#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
import random
import time
#ejemplo1
def funcion_parametro(valor):
    print(f"Adios {valor}")

def funcion_principal(funcion,valor):
    print(f"Hola {valor}")
    return funcion(valor)


funcion_principal(funcion_parametro,"Yuan")


#ejemplo2

def suma(numeros):
    lista_nueva = [num*2 for num in numeros]
    print(f"Nueva lista(x2): {lista_nueva}")
    print(f"Suma total: {sum(lista_nueva)}")

def SumaPrincipal(funcion,numeros):
    print(f"Numeros a sumar su doble : {numeros}")
    return funcion(numeros)

lista1 = [1,2,3]

SumaPrincipal(suma,lista1)


#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Debe notificar que el plato está listo o ha sido entregado.
#  */


def funcion_pedido(confirmacion,listo,entrega):
    comida = input("Ingrese nombre de plato: ")
    print("Procesando pedido...")

    confirmacion(comida)
    listo(comida)
    entrega(comida)

def confirmacion(comida):
    tiempo = random.randint(1,10)
    print(f"Confirmando pedido de {comida} en {tiempo}....")
    time.sleep(tiempo)
    print(f"Pedido de {comida} confirmado")

    
def listo(comida):
    tiempo_preparacion = random.randint(1,10)
    print(f"Preparando {comida} en {tiempo_preparacion} segundos ....")
    time.sleep(tiempo_preparacion)
    print(f"Pedido de {comida} listo")


def entrega(comida):
    tiempo_entrega = random.randint(1,10)
    print(f"Entregando plato en {tiempo_entrega} segundos ....")
    time.sleep(tiempo_entrega)
    print(f"Plato de {comida} entregado")





#solucion usando cadena de callbacks
# def funcion_pedido(callback_confirmacion):
#     comida = input("Ingrese el nombre del plato: ")
#     print("Procesando pedido...")

#     # Inicia la cadena de callbacks llamando a confirmacion
#     callback_confirmacion(comida, listo, entrega)

# def confirmacion(comida, callback_listo, callback_entrega):
#     tiempo = random.randint(1, 10)
#     print(f"Confirmando pedido de {comida} en {tiempo} segundos...")
#     time.sleep(tiempo)
#     print(f"Pedido de {comida} confirmado.")

#     # Llama al siguiente callback pasando el callback para la preparación
#     callback_listo(comida, callback_entrega)

# def listo(comida, callback_entrega):
#     tiempo = random.randint(1, 10)
#     print(f"Preparando {comida} en {tiempo} segundos...")
#     time.sleep(tiempo)
#     print(f"El plato {comida} está listo.")

#     # Llama al callback de entrega
#     callback_entrega(comida)

# def entrega(comida):
#     tiempo = random.randint(1, 10)
#     print(f"Entregando {comida} en {tiempo} segundos...")
#     time.sleep(tiempo)
#     print(f"El plato {comida} ha sido entregado.")


funcion_pedido(confirmacion,listo,entrega)
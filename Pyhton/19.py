# /*
#  * EJERCICIO:
#  * Empleando tu lenguaje, explora la definición del tipo de dato
#  * que sirva para definir enumeraciones (Enum).
#  * Crea un Enum que represente los días de la semana del lunes
#  * al domingo, en ese orden. Con ese enumerado, crea una operación
#  * que muestre el nombre del día de la semana dependiendo del número entero
#  * utilizado (del 1 al 7).
#  *

from enum import Enum,StrEnum
#Enum usando clases
print("_______________________________________")
print("USANDO CLASES CON ENUM")
class DiasSemana(Enum):
    LUNES = 1
    MARTES=2
    MIERCOLES=3
    JUEVES=4
    VIERNES=5
    SABADO=6
    DOMINGO=7

def determinar_semana(numero):
    try:
        return DiasSemana(numero).name
    except ValueError:
        print("Numero invalido, ingresa del 1 al 7")

print(determinar_semana(5))

print("_______________________________________")
print("USANDO DIRECTAMENTE ENUM")

DiasSemana2 =Enum('DiasSemana2', ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'])

print(DiasSemana2(4).name)
    



#  * DIFICULTAD EXTRA (opcional):
#  * Crea un pequeño sistema de gestión del estado de pedidos.
#  * Implementa una clase que defina un pedido con las siguientes características:
#  * - El pedido tiene un identificador y un estado.
#  * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
#  * - Implementa las funciones que sirvan para modificar el estado:
#  *   - Pedido enviado
#  *   - Pedido cancelado
#  *   - Pedido entregado
#  *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
#  * - Implementa una función para mostrar un texto descriptivo según el estado actual.
#  * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
#  */


class EstadoPedido(Enum):
    PENDIENTE = 1 
    ENVIADO = 2
    ENTREGADO = 3
    CANCELADO = 4


class Orden:
    def __init__(self,id,estado= EstadoPedido.PENDIENTE):
        self.id = id
        self.estado = estado
    
    def enviado(self):
        if self.estado == EstadoPedido.PENDIENTE:
            self.estado = EstadoPedido.ENVIADO
            print("Orden enviada")
        else:
            print("La orden ya fue enviado, cancelado o entregado")
        

    def cancelado(self):
        if self.estado != EstadoPedido.ENTREGADO and self.estado != EstadoPedido.CANCELADO:
            self.estado = EstadoPedido.CANCELADO
            print("Orden cancelada")
        else:
            print("La orden ya esta cancelada o entregada")

        pass
    def entregado(self):
        if self.estado == EstadoPedido.ENVIADO:
            self.estado = EstadoPedido.ENTREGADO
            print("Orden entregada")
        else:
            print("La pedido ya fue entregado o esta en una etapa anterior")
        pass
    
    def mostrar_estado(self):
        print(f"Pedido: {self.id}, Estado:{self.estado.name}")

orden1 = Orden(1)
orden2 = Orden(2,EstadoPedido.ENVIADO)
orden3 = Orden(3,EstadoPedido.CANCELADO)

orden1.mostrar_estado()
orden2.mostrar_estado()

orden1.enviado()
orden1.mostrar_estado()

orden3.cancelado()
orden3.mostrar_estado()
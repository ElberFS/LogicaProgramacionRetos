<?php
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
 */

 // EJERCICIO: Enumeraciones en PHP

enum DiasSemana: int {
    case LUNES = 1;
    case MARTES = 2;
    case MIERCOLES = 3;
    case JUEVES = 4;
    case VIERNES = 5;
    case SABADO = 6;
    case DOMINGO = 7;
}

function obtenerNombreDia(int $numero): string {
    return DiasSemana::tryFrom($numero)?->name ?? "Día inválido";
}

echo "El día 3 es: " . obtenerNombreDia(3) . "\n";

echo "\nDIFICULTAD EXTRA: Sistema de gestión de pedidos\n";

enum EstadoPedido: string {
    case PENDIENTE = "Pendiente";
    case ENVIADO = "Enviado";
    case ENTREGADO = "Entregado";
    case CANCELADO = "Cancelado";
}

class Pedido {
    public int $id;
    public EstadoPedido $estado;

    public function __construct(int $id) {
        $this->id = $id;
        $this->estado = EstadoPedido::PENDIENTE;
    }

    public function enviar() {
        if ($this->estado === EstadoPedido::PENDIENTE) {
            $this->estado = EstadoPedido::ENVIADO;
            echo "Pedido {$this->id} ha sido enviado.\n";
        } else {
            echo "No se puede enviar el pedido {$this->id} en su estado actual ({$this->estado->value}).\n";
        }
    }

    public function entregar() {
        if ($this->estado === EstadoPedido::ENVIADO) {
            $this->estado = EstadoPedido::ENTREGADO;
            echo "Pedido {$this->id} ha sido entregado.\n";
        } else {
            echo "No se puede entregar el pedido {$this->id} en su estado actual ({$this->estado->value}).\n";
        }
    }

    public function cancelar() {
        if ($this->estado === EstadoPedido::PENDIENTE || $this->estado === EstadoPedido::ENVIADO) {
            $this->estado = EstadoPedido::CANCELADO;
            echo "Pedido {$this->id} ha sido cancelado.\n";
        } else {
            echo "No se puede cancelar el pedido {$this->id} en su estado actual ({$this->estado->value}).\n";
        }
    }

    public function mostrarEstado() {
        echo "Estado del pedido {$this->id}: {$this->estado->value}\n";
    }
}

$pedido1 = new Pedido(101);
$pedido1->mostrarEstado();
$pedido1->enviar();
$pedido1->entregar();
$pedido1->cancelar(); // No debería permitir cancelar porque ya está entregado

$pedido2 = new Pedido(102);
$pedido2->mostrarEstado();
$pedido2->cancelar(); // Debería permitir cancelar porque está pendiente
<?php

/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

// EJERCICIO: Ejemplo de Callback en PHP

function ejecutarCallback($mensaje, callable $callback) {
    echo "Mensaje inicial: $mensaje\n";
    $callback();
}

ejecutarCallback("Hola, esto es un callback", function() {
    echo "Ejecutando la función callback.\n";
});


// DIFICULTAD EXTRA: Simulador de pedidos de restaurante con Callbacks

function procesarPedido($plato, callable $confirmacion, callable $listo, callable $entrega) {
    echo "Procesando pedido de: $plato\n";
    $confirmacion($plato);
    
    $tiempoPreparacion = rand(1, 10);
    sleep($tiempoPreparacion);
    $listo($plato);
    
    $tiempoEntrega = rand(1, 5);
    sleep($tiempoEntrega);
    $entrega($plato);
}

procesarPedido(
    "Pizza Margherita",
    function($plato) {
        echo "Confirmación: Su pedido de $plato ha sido recibido.\n";
    },
    function($plato) {
        echo "Listo: Su $plato está listo para ser servido.\n";
    },
    function($plato) {
        echo "Entrega: Su $plato ha sido entregado. ¡Disfrute su comida!\n";
    }
);

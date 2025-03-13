<?php 

/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */


function imprimirNumeros($n) {
    // Caso base: si n es menor que 0, detenemos la recursión
    if ($n < 0) {
        return;
    }

    // Mostramos el número actual
    echo $n . "\n";

    // Llamada recursiva con el siguiente número decreciente
    imprimirNumeros($n - 1);
}

// Llamamos a la función con 100
imprimirNumeros(100);
/************************************************************************************ */
/*DIFICULTAD EXTRA (opcional): */
/************************************************************************************ */
function factorial($n) {
    // Caso base: el factorial de 0 o 1 es 1
    if ($n <= 1) {
        return 1;
    }

    // Caso recursivo: n! = n * (n-1)!
    return $n * factorial($n - 1);
}

// Probar con un número
$numero = 5;
echo "Factorial de $numero es: " . factorial($numero) . "\n";
/************************************************************************************ */
function fibonacci($n) {
    // Caso base: los dos primeros términos de Fibonacci
    if ($n == 0) return 0;
    if ($n == 1) return 1;

    // Caso recursivo: suma de los dos términos anteriores
    return fibonacci($n - 1) + fibonacci($n - 2);
}

// Probar con un número
$posicion = 7;
echo "Fibonacci en la posición $posicion es: " . fibonacci($posicion) . "\n";

/************************************************************************************ */
function fibonacciMemo($n, &$memo = []) {
    // Si ya calculamos el valor, lo retornamos
    if (isset($memo[$n])) return $memo[$n];

    // Caso base
    if ($n == 0) return 0;
    if ($n == 1) return 1;

    // Guardamos el resultado en la memoria para futuras llamadas
    return $memo[$n] = fibonacciMemo($n - 1, $memo) + fibonacciMemo($n - 2, $memo);
}

// Probar con un número grande
$posicion = 40;
echo "Fibonacci en la posición $posicion es: " . fibonacciMemo($posicion) . "\n";
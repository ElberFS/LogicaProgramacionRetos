<?php
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Por valor (tipos primitivos)
$a = 10;
$b = $a; // Se copia el valor
$b = 20;
echo "a: $a, b: $b". "\n";// a: 10, b: 20

// Por referencia (objetos y referencias explícitas)
$c = 10;
$d = &$c; // Se referencia a la misma dirección en memoria
$d = 30;
echo "c: $c, d: $d". "\n"; // c: 30, d: 30


// Paso por valor
function modificarValor($x) {
    $x = 100;
}
$numero = 50;
modificarValor($numero);
echo $numero. "\n"; // 50 (No cambia)

// Paso por referencia
function modificarReferencia(&$x) {
    $x = 100;
}
$numero = 50;
modificarReferencia($numero);
echo $numero . "\n"; // 100 (Cambia)


//  DIFICULTAD EXTRA

// Intercambio por valor (no modifica las originales)
function intercambiarPorValor($a, $b) {
    return [$b, $a]; // Retorna los valores intercambiados
}

// Intercambio por referencia (modifica las originales)
function intercambiarPorReferencia(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
}

// Variables originales
$x = 5;
$y = 10;

// Paso por valor
list($nuevoX, $nuevoY) = intercambiarPorValor($x, $y);
echo "Por Valor -> Original: x=$x, y=$y | Intercambiados: x=$nuevoX, y=$nuevoY\n";

// Paso por referencia
intercambiarPorReferencia($x, $y);
echo "Por Referencia -> Modificados: x=$x, y=$y\n";
<?php 
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

// EJERCICIO: Iterar números del 1 al 10 con diferentes mecanismos

// 1. Usando un bucle for
echo "Usando for:\n";
for ($i = 1; $i <= 10; $i++) {
    echo $i . " ";
}
echo "\n\n";

// 2. Usando un bucle while
echo "Usando while:\n";
$i = 1;
while ($i <= 10) {
    echo $i . " ";
    $i++;
}
echo "\n\n";

// 3. Usando un bucle do-while
echo "Usando do-while:\n";
$i = 1;
do {
    echo $i . " ";
    $i++;
} while ($i <= 10);
echo "\n\n";

// DIFICULTAD EXTRA: Más formas de iterar

// 4. Usando un array con foreach
echo "Usando foreach:\n";
$numeros = range(1, 10);
foreach ($numeros as $num) {
    echo $num . " ";
}
echo "\n\n";

// 5. Usando un generador con yield
echo "Usando generador:\n";
function generarNumeros() {
    for ($i = 1; $i <= 10; $i++) {
        yield $i;
    }
}
foreach (generarNumeros() as $num) {
    echo $num . " ";
}
echo "\n\n";

// 6. Usando array_map
echo "Usando array_map:\n";
array_map(fn($num) => print($num . " "), range(1, 10));
echo "\n\n";

// 7. Usando una función recursiva
echo "Usando recursividad:\n";
function imprimirRecursivo($n) {
    if ($n > 10) return;
    echo $n . " ";
    imprimirRecursivo($n + 1);
}
imprimirRecursivo(1);
echo "\n\n";

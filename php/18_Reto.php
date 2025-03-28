<?php
/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */

// EJERCICIO: Operaciones con conjuntos en PHP

// Crear un conjunto de datos (array en PHP)
$datos = ["manzana", "banana", "uva", "pera"];

echo "Conjunto inicial: ";
print_r($datos);

// Añadir un elemento al final
$datos[] = "naranja";
echo "\nDespués de añadir al final: ";
print_r($datos);

// Añadir un elemento al principio
array_unshift($datos, "kiwi");
echo "\nDespués de añadir al principio: ";
print_r($datos);

// Añadir varios elementos en bloque al final
array_push($datos, "mango", "papaya");
echo "\nDespués de añadir varios al final: ";
print_r($datos);

// Añadir varios elementos en una posición concreta
array_splice($datos, 2, 0, ["cereza", "fresa"]);
echo "\nDespués de añadir varios en una posición concreta: ";
print_r($datos);

// Eliminar un elemento en una posición concreta
unset($datos[3]);
$datos = array_values($datos); // Reindexar el array
echo "\nDespués de eliminar en una posición concreta: ";
print_r($datos);

// Actualizar un valor en una posición concreta
$datos[1] = "sandía";
echo "\nDespués de actualizar un valor en una posición concreta: ";
print_r($datos);

// Comprobar si un elemento está en el conjunto
echo "\n¿Existe 'mango' en el conjunto?: " . (in_array("mango", $datos) ? "Sí" : "No") . "\n";

// Eliminar todo el contenido del conjunto
$datos = [];
echo "\nDespués de eliminar todo el contenido: ";
print_r($datos);

// DIFICULTAD EXTRA: Operaciones con conjuntos

$conjuntoA = ["rojo", "azul", "verde", "amarillo"];
$conjuntoB = ["verde", "amarillo", "negro", "blanco"];

// Unión
echo "\nUnión: ";
print_r(array_unique(array_merge($conjuntoA, $conjuntoB)));

// Intersección
echo "\nIntersección: ";
print_r(array_intersect($conjuntoA, $conjuntoB));

// Diferencia
echo "\nDiferencia (A - B): ";
print_r(array_diff($conjuntoA, $conjuntoB));

echo "\nDiferencia (B - A): ";
print_r(array_diff($conjuntoB, $conjuntoA));

// Diferencia simétrica
echo "\nDiferencia simétrica: ";
print_r(array_merge(array_diff($conjuntoA, $conjuntoB), array_diff($conjuntoB, $conjuntoA)));
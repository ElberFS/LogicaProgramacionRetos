<?php
/*

#02 FUNCIONES Y ALCANCE
* Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
*/


function imprimirNumeros(string $texto1, string $texto2): int {  // :int hace que siempre devolvera un numero entero
    $contador = 0;
    
    for ($i = 1; $i <= 100; $i++) {
        if ($i % 3 == 0 && $i % 5 == 0) {
            echo $texto1 . $texto2 . "\n";
        } elseif ($i % 3 == 0) {
            echo $texto1 . "\n";
        } elseif ($i % 5 == 0) {
            echo $texto2 . "\n";
        } else {
            echo $i . "\n";
            $contador++;
        }
    }
    
    return $contador;
}

// Ejemplo de uso
$vecesImpresas = imprimirNumeros("Prueba01", "Prueba02");
echo "Números impresos: $vecesImpresas\n";

?>
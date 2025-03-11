¿<?php
/*
#04 CADENAS DE CARACTERES
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


// Operaciones con cadenas en PHP

$texto01= "Operacion con cadenas";

echo "texto original:  $texto01\n";

# 1. Acceso a caracteres especificos
echo "1. Segundo Caracter: " . $texto01[2] . "\n";

# 2. Subcadenas 
echo "2. Subcadenas: " .substr($texto01,0,9) . "\n";

# 3. Longitud 
echo "3. Longitud: " .strlen($texto01) ."\n";

# 4. Concatenacion
$texto02 = "para el reto #4";
$contanacion = $texto01 . $texto02 ; 
echo "4. Concatenacion: " .$texto01 ." " . $texto02 ."\n";
echo "4.1 Otra opcion de concatenacion: " . $contanacion."\n";

# 5. Repetición 
$texto_repetido = str_repeat($texto01 , 3); 
echo "5. Repeticion: " . $texto_repetido ."\n";

# 6. Recorrido
for ($i = 0; $i < strlen($texto01); $i++) {
    echo "Posicion del Caracter " . $i . ": " .$texto01[ $i ] ."\n";
};

# 7. Conversión a mayúsculas y minúsculas
$mayusculas = strtoupper($texto01);
$minusculas = strtolower($texto02);

echo "7 . Mayusculas : " . $mayusculas . " Minusculas: " . $minusculas ."\n";


# 8-9. División las separo con un espacio
$division_texto = explode(" ",$texto01);
# y hago una union con implode
/*
las separo con un espacio y las junto con una ,
*/
echo "8-9 . Resultado : " . implode("-",$division_texto). "\n";

# 10. Interpolacion
$nombre = "elber";
$edad = 12 ;
$mensaje = "yo soy  $nombre y tengo $edad años.";
echo "10. Mensaje interpolado: " .$mensaje ."\n"; 

# 11. Verificacion
$verificacion_texto = strpos($texto01 , "Cadena") !=false;
echo "El texto contine la palabra -> Cadena " . ($verificacion_texto?'Sí' : 'No' ) ."\n";

/* RETO EXTRA EJECICIO 
Programa para detectar palindromo  , anagrama , isograma
Un pa
Un anagrama es una palabra o frase formada al reorganizar las letras de otra palabra o frase.
Un isograma es una palabra en la que ninguna letra se repite.
*/



// Definimos las funciones antes de usarlas

function Palindromo($palabra) {
    // Convertir a minúsculas y eliminar espacios
    $palabra = mb_strtolower($palabra, 'UTF-8');
    $palabra = str_replace(' ', '', $palabra);

    // Eliminar tildes y caracteres especiales
    $palabra = preg_replace('/[^\p{L}0-9]/u', '', $palabra);

    // Comparar con la versión invertida
    return $palabra === strrev($palabra) ? "Sí, es un palíndromo" : "No, no es un palíndromo";
}

function Anagrama($palabra1, $palabra2) {
    // Convertimos todo a minúsculas y eliminamos espacios
    $p1 = str_replace(' ', '', mb_strtolower($palabra1, 'UTF-8'));
    $p2 = str_replace(' ', '', mb_strtolower($palabra2, 'UTF-8'));

    // Convertimos en arrays y ordenamos
    $ordenPalabra1 = str_split($p1);
    $ordenPalabra2 = str_split($p2);
    sort($ordenPalabra1);
    sort($ordenPalabra2);

    return $ordenPalabra1 === $ordenPalabra2 ? "Sí, es un anagrama" : "No, no es un anagrama";
}

function Isograma($palabra) {
    // Convertir a minúsculas y eliminar espacios
    $palabra = mb_strtolower($palabra, 'UTF-8');
    $palabra = str_replace(' ', '', $palabra);

    // Eliminar tildes y caracteres especiales
    $palabra = preg_replace('/[^\p{L}]/u', '', $palabra);

    // Crear un array para almacenar las letras ya vistas
    $letras = [];

    // Recorrer cada letra de la palabra
    foreach (mb_str_split($palabra) as $letra) {
        if (in_array($letra, $letras)) {
            return "No, no es un isograma";
        }
        $letras[] = $letra;
    }

    return "Sí, es un isograma";
}

// Ahora ejecutamos el código después de definir las funciones

echo "Palabras a Analizar:\n\n";

echo Palindromo("reconocer") . "\n";
echo Palindromo("casa") . "\n";

echo Anagrama("amor", "Roma") . "\n";
echo Anagrama("gato", "perro") . "\n";

echo Isograma("murciélago") . "\n";
echo Isograma("casa") . "\n";

?>


<?php

/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

 // EJERCICIO: Realizar una petición HTTP en PHP

$url = "https://jsonplaceholder.typicode.com/posts/1";
$response = file_get_contents($url);

if ($response !== false) {
    echo "Petición exitosa:\n";
    echo $response;
} else {
    echo "Error en la petición.";
}

echo "\n\nDIFICULTAD EXTRA: Obtener información de un Pokémon con la PokéAPI\n";

function obtenerPokemon(string $nombre) {
    $url = "https://pokeapi.co/api/v2/pokemon/" . strtolower($nombre);
    $response = file_get_contents($url);
    
    if ($response === false) {
        echo "Error al obtener el Pokémon.\n";
        return;
    }
    
    $data = json_decode($response, true);
    
    echo "Nombre: " . ucfirst($data["name"]) . "\n";
    echo "ID: " . $data["id"] . "\n";
    echo "Peso: " . $data["weight"] . "\n";
    echo "Altura: " . $data["height"] . "\n";
    
    echo "Tipos: ";
    foreach ($data["types"] as $type) {
        echo ucfirst($type["type"]["name"]) . " ";
    }
    echo "\n";
}

obtenerPokemon("pikachu");
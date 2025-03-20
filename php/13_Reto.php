<?php 

/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

/**
 * Función que suma dos números enteros y devuelve el resultado.
 *
 * @param int $a Primer número a sumar.
 * @param int $b Segundo número a sumar.
 * @return int Resultado de la suma.
 */
function sumar(int $a, int $b): int {
    return $a + $b;
}

// Pruebas manuales con assert()
assert(sumar(3, 5) === 8);
assert(sumar(-2, -4) === -6);
assert(sumar(7, -3) === 4);
assert(sumar(0, 5) === 5);

echo "Prueba 1: " . (sumar(3, 5) === 8 ? "✅ Correcto" : "❌ Error") . "\n";
echo "Prueba 2: " . (sumar(-2, -4) === -6 ? "✅ Correcto" : "❌ Error") . "\n";
echo "Prueba 3: " . (sumar(7, -3) === 4 ? "✅ Correcto" : "❌ Error") . "\n";
echo "Prueba 4: " . (sumar(0, 5) === 5 ? "✅ Correcto" : "❌ Error") . "\n";


// Dificultad extra

/**
 * Diccionario con información personal.
 */
$datos = [
    "name" => "Juan Pérez",
    "age" => 25,
    "birth_date" => "1999-03-15",
    "programming_languages" => ["PHP", "JavaScript", "Python"]
];

/**
 * Función para verificar si existen todas las claves en el diccionario.
 *
 * @param array $datos Diccionario a verificar.
 * @return bool Retorna true si todas las claves existen, false en caso contrario.
 */
function validarCampos(array $datos): bool {
    $claves_requeridas = ["name", "age", "birth_date", "programming_languages"];
    foreach ($claves_requeridas as $clave) {
        if (!array_key_exists($clave, $datos)) {
            return false;
        }
    }
    return true;
}

/**
 * Función para validar los valores de los datos.
 *
 * @param array $datos Diccionario a validar.
 * @return bool Retorna true si los datos son correctos, false en caso contrario.
 */
function validarDatos(array $datos): bool {
        return is_string($datos["name"]) &&
            is_int($datos["age"]) &&
            preg_match("/\d{4}-\d{2}-\d{2}/", $datos["birth_date"]) &&
            is_array($datos["programming_languages"]);
}

/**
 * Pruebas manuales con assert().
 */
assert(validarCampos($datos) === true);
assert(validarDatos($datos) === true);

echo "Prueba Campos: " . (validarCampos($datos) === true ? "✅ Correcto" : "❌ Error") . "\n";
echo "Prueba Datos: " . (validarDatos($datos) === true ? "✅ Correcto" : "❌ Error") . "\n";


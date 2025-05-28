<?php
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

// EJERCICIO: Expresiones regulares en PHP

// Función para extraer todos los números de un texto
function extraerNumeros($texto) {
    preg_match_all('/\d+/', $texto, $matches);
    return $matches[0];
}

$texto = "Hoy es 28 de marzo de 2025 y son las 14:30 horas.";
$numeros = extraerNumeros($texto);
echo "Números encontrados: " . implode(", ", $numeros) . "\n";

// DIFICULTAD EXTRA: Validaciones con expresiones regulares

// 1. Validar un email
function validarEmail($email) {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}

// 2. Validar un número de teléfono (formato internacional: +XX XXXX XXXX)
function validarTelefono($telefono) {
    return preg_match('/^\+?[0-9]{1,3}[ -]?[0-9]{4,14}$/', $telefono);
}

// 3. Validar una URL
function validarURL($url) {
    return filter_var($url, FILTER_VALIDATE_URL) !== false;
}

// Pruebas
$email = "ejemplo@correo.com";
$telefono = "+51 987654321";
$url = "https://www.ejemplo.com";

echo "Email válido: " . (validarEmail($email) ? "Sí" : "No") . "\n";
echo "Teléfono válido: " . (validarTelefono($telefono) ? "Sí" : "No") . "\n";
echo "URL válida: " . (validarURL($url) ? "Sí" : "No") . "\n";
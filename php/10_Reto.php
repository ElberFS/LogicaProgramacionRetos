<?php

/*
* EXCEPCIONES
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado. 
 */


// Habilitar la visualización de errores (para desarrollo, desactívalo en producción)
error_reporting(E_ALL);
ini_set('display_errors', 1);

echo "Inicio del script\n";

// Manejo de excepción para división por cero
try {
    $numerador = 10;
    $denominador = 0; // Error intencional
    
    if ($denominador == 0) {
        throw new Exception("Error: División por cero no permitida.");
    }

    $resultado = $numerador / $denominador;
    echo "Resultado: $resultado\n";

} catch (Exception $e) {
    // Capturar y manejar la excepción
    echo "Excepción atrapada: " . $e->getMessage() . "\n";
} finally {
    // Código que siempre se ejecuta
    echo "Finalizando bloque de división.\n";
}

// Manejo de excepción para acceso a índice inexistente en un array
try {
    $array = [1, 2, 3];
    
    if (!isset($array[10])) {
        throw new OutOfBoundsException("Error: Índice fuera de los límites del array.");
    }

    echo "Valor en índice 10: " . $array[10] . "\n";

} catch (OutOfBoundsException $e) {
    echo "Excepción atrapada: " . $e->getMessage() . "\n";
} finally {
    echo "Finalizando acceso al array.\n";
}

echo "Fin del script\n";


/* Dificultad Extra */

function procesarParametros($param1, $param2) {
    try {
        if ($param1 < 0) {
            throw new InvalidArgumentException("Error: El primer parámetro no puede ser negativo.");
        }
        
        if ($param2 == 0) {
            throw new Exception("Error: El segundo parámetro no puede ser cero.");
        }
        
        if ($param2 > 10) {
            throw new RuntimeException("Error: El segundo parámetro no puede ser mayor a 10.");
        }
        
        echo "Parámetros procesados correctamente.\n";
        
    } catch (InvalidArgumentException $e) {
        echo "Excepción atrapada: " . $e->getMessage() . "\n";
    } catch (Exception $e) {
        echo "Excepción atrapada: " . $e->getMessage() . "\n";
    } catch (RuntimeException $e) {
        echo "Excepción atrapada: " . $e->getMessage() . "\n";
    } finally {
        echo "Finalizando procesamiento de parámetros.\n";
    }
}

//ejemplo de uso
procesarParametros(-5, 0);
procesarParametros(5, 0);
procesarParametros(5, 15);
procesarParametros(5, 5);
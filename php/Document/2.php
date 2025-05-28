<?php

/**
 * Ejemplo de Conexión a Base de Datos PHP con MySQLi (Orientado a Objetos)
 *
 * Este script demuestra cómo establecer una conexión a la base de datos utilizando MySQLi (estilo orientado a objetos).
 * Incluye manejo de errores y preparación para la vinculación de parámetros.
 */

// --- Configuración de la Base de Datos ---
$host = 'localhost'; // O la dirección IP de tu servidor MySQL
$port = 3307;        // Puerto de MySQL (el que especificaste)
$dbname = 'prueba';  // Nombre de la base de datos (la que vamos a crear)
$user = 'root';      // Usuario de la base de datos (generalmente 'root' por defecto, cámbialo si es diferente)
$password = 'elber'; // Contraseña de la base de datos (la que especificaste)

// Intentar establecer una nueva conexión MySQLi
// El '@' suprime el mensaje de error predeterminado de PHP en caso de fallo de conexión,
// permitiéndonos manejarlo nosotros mismos.
$mysqli = @new mysqli($host, $user, $password, $dbname, $port);

// Verificar si la conexión fue exitosa
if ($mysqli->connect_errno) {
    // La conexión falló, registra el error y termina el script
    error_log("Error de Conexión a la Base de Datos (MySQLi): " . $mysqli->connect_error);
    die("Fallo la conexión a la base de datos. Por favor, inténtalo de nuevo más tarde. (Código de Error: " . $mysqli->connect_errno . ")");
}

echo "¡Conexión a la base de datos '$dbname' mediante MySQLi exitosa! \n";

// Establecer el conjunto de caracteres a UTF-8 para una codificación correcta
// (importante para caracteres internacionales, tildes, ñ, etc.)
if (!$mysqli->set_charset("utf8mb4")) {
    error_log("Error al cargar el conjunto de caracteres utf8mb4: " . $mysqli->error);
    // Podrías querer manejar este error de forma más elegante dependiendo de tu aplicación
}


// --- Ejemplo: Preparando una sentencia y vinculando parámetros (para uso futuro) ---
// Así es como prepararías una consulta para prevenir la inyección SQL.
// Descomenta y modifica para operaciones reales de base de datos.

/*
// Prepara la sentencia SQL con marcadores de posición (signos de interrogación)
if ($stmt = $mysqli->prepare("SELECT * FROM tu_tabla WHERE id = ? AND nombre = ?")) {
    // Vincula los parámetros a los marcadores de posición.
    // "is" significa: 'i' para entero (integer), 's' para cadena (string).
    $id = 1;
    $nombre = 'Nombre de Ejemplo';
    $stmt->bind_param("is", $id, $nombre);

    // Ejecuta la sentencia
    $stmt->execute();

    // Obtiene el resultado de la consulta
    $result = $stmt->get_result();

    // Recorre y muestra las filas
    while ($row = $result->fetch_assoc()) {
        print_r($row);
    }

    // Cierra la sentencia
    $stmt->close();
} else {
    // Error al preparar la sentencia
    error_log("Error de Preparación MySQLi: " . $mysqli->error);
    die("Error al preparar la consulta de la base de datos.");
}
*/

// Ahora puedes usar el objeto $mysqli para interactuar con la base de datos (ej. $mysqli->query(), $mysqli->prepare())

// Cerrar la conexión (importante para liberar recursos)
$mysqli->close();

?>
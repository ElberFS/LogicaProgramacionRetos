<?php
/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 */

// Datos de la persona a almacenar

/**
 * Programa en PHP para generar archivos XML y JSON con datos de una persona,
 * mostrar su contenido y luego eliminarlos.
 */

// Datos de la persona a almacenar
$persona = [
    'nombre' => 'Juan Pérez',
    'edad' => 30,
    'fecha_nacimiento' => '1994-05-15',
    'lenguajes' => ['PHP', 'JavaScript', 'Python']
];

/**
 * Función para crear y guardar datos en un archivo XML
 */
function crearXML($persona, $archivoXML) {
    // Crear un nuevo objeto DOMDocument
    $xml = new DOMDocument("1.0", "UTF-8");
    $xml->formatOutput = true;

    // Crear el nodo raíz
    $raiz = $xml->createElement("persona");
    $xml->appendChild($raiz);

    // Crear los elementos y añadirlos al XML
    foreach ($persona as $clave => $valor) {
        if (is_array($valor)) {
            $nodoLista = $xml->createElement($clave);
            foreach ($valor as $item) {
                $nodoItem = $xml->createElement("lenguaje", $item);
                $nodoLista->appendChild($nodoItem);
            }
            $raiz->appendChild($nodoLista);
        } else {
            $nodo = $xml->createElement($clave, $valor);
            $raiz->appendChild($nodo);
        }
    }

    // Guardar el archivo XML
    $xml->save($archivoXML);
}

/**
 * Función para crear y guardar datos en un archivo JSON
 */
function crearJSON($persona, $archivoJSON) {
    $json = json_encode($persona, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
    file_put_contents($archivoJSON, $json);
}

/**
 * Función para mostrar el contenido de un archivo
 */
function mostrarContenidoArchivo($archivo) {
    if (file_exists($archivo)) {
        echo "Contenido de $archivo:\n";
        echo file_get_contents($archivo) . "\n\n";
    } else {
        echo "El archivo $archivo no existe.\n";
    }
}

/**
 * Función para eliminar archivos
 */
function borrarArchivo($archivo) {
    if (file_exists($archivo)) {
        unlink($archivo);
        echo "El archivo $archivo ha sido eliminado.\n";
    } else {
        echo "El archivo $archivo no existe.\n";
    }
}

// Definir nombres de archivos
$archivoXML = "persona.xml";
$archivoJSON = "persona.json";

// Crear archivos
crearXML($persona, $archivoXML);
crearJSON($persona, $archivoJSON);

// Mostrar contenido de los archivos
mostrarContenidoArchivo($archivoXML);
mostrarContenidoArchivo($archivoJSON);

// Borrar archivos
borrarArchivo($archivoXML);
borrarArchivo($archivoJSON);



// Difucultad extra

/**
 * Programa en PHP para generar archivos XML y JSON con datos de una persona,
 * mostrar su contenido y luego eliminarlos.
 */

class Persona {
    public $nombre;
    public $edad;
    public $fecha_nacimiento;
    public $lenguajes;

    public function __construct($nombre, $edad, $fecha_nacimiento, $lenguajes) {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->fecha_nacimiento = $fecha_nacimiento;
        $this->lenguajes = $lenguajes;
    }

    /**
     * Método para crear y guardar datos en un archivo XML
     */
    public function guardarComoXML($archivoXML) {
        $xml = new DOMDocument("1.0", "UTF-8");
        $xml->formatOutput = true;

        $raiz = $xml->createElement("persona");
        $xml->appendChild($raiz);

        $raiz->appendChild($xml->createElement("nombre", $this->nombre));
        $raiz->appendChild($xml->createElement("edad", $this->edad));
        $raiz->appendChild($xml->createElement("fecha_nacimiento", $this->fecha_nacimiento));

        $nodoLista = $xml->createElement("lenguajes");
        foreach ($this->lenguajes as $lenguaje) {
            $nodoLista->appendChild($xml->createElement("lenguaje", $lenguaje));
        }
        $raiz->appendChild($nodoLista);

        $xml->save($archivoXML);
    }

    /**
     * Método para crear y guardar datos en un archivo JSON
     */
    public function guardarComoJSON($archivoJSON) {
        $json = json_encode($this, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE);
        file_put_contents($archivoJSON, $json);
    }

    /**
     * Método para leer un archivo XML y convertirlo en un objeto Persona
     */
    public static function leerDesdeXML($archivoXML) {
        if (!file_exists($archivoXML)) return null;

        $xml = simplexml_load_file($archivoXML);
        $nombre = (string) $xml->nombre;
        $edad = (int) $xml->edad;
        $fecha_nacimiento = (string) $xml->fecha_nacimiento;
        $lenguajes = [];
        foreach ($xml->lenguajes->lenguaje as $lenguaje) {
            $lenguajes[] = (string) $lenguaje;
        }

        return new Persona($nombre, $edad, $fecha_nacimiento, $lenguajes);
    }

    /**
     * Método para leer un archivo JSON y convertirlo en un objeto Persona
     */
    public static function leerDesdeJSON($archivoJSON) {
        if (!file_exists($archivoJSON)) return null;

        $datos = json_decode(file_get_contents($archivoJSON), true);
        return new Persona($datos['nombre'], $datos['edad'], $datos['fecha_nacimiento'], $datos['lenguajes']);
    }
}

// Crear instancia de Persona
$persona = new Persona("Juan Pérez", 30, "1994-05-15", ["PHP", "JavaScript", "Python"]);

// Definir nombres de archivos
$archivoXML = "persona.xml";
$archivoJSON = "persona.json";

// Guardar en archivos
$persona->guardarComoXML($archivoXML);
$persona->guardarComoJSON($archivoJSON);

// Leer desde archivos y reconstruir objetos
$personaDesdeXML = Persona::leerDesdeXML($archivoXML);
$personaDesdeJSON = Persona::leerDesdeJSON($archivoJSON);

// Mostrar contenido de los objetos leídos
echo "\nDatos desde XML:";
print_r($personaDesdeXML);

echo "\nDatos desde JSON:";
print_r($personaDesdeJSON);

// Borrar archivos
unlink($archivoXML);
unlink($archivoJSON);
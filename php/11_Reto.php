<?php

/*
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */


 // Definir el nombre del archivo con el nombre de usuario de GitHub
$usuarioGithub = "TuUsuarioGitHub"; 
$nombreArchivo = "$usuarioGithub.txt";

// Contenido del archivo
$contenido = "Nombre: Tu Nombre\n"; 
$contenido .= "Edad: Tu Edad\n"; 
$contenido .= "Lenguaje favorito: PHP\n";

// Crear y escribir en el archivo
if (file_put_contents($nombreArchivo, $contenido) !== false) {
    echo "Archivo '$nombreArchivo' creado exitosamente.\n";
} else {
    echo "Error al crear el archivo.\n";
    exit();
}

// Leer e imprimir el contenido del archivo
$contenidoLeido = file_get_contents($nombreArchivo);
if ($contenidoLeido !== false) {
    echo "Contenido del archivo:\n";
    echo $contenidoLeido;
} else {
    echo "Error al leer el archivo.\n";
}

// Eliminar el archivo
if (unlink($nombreArchivo)) {
    echo "Archivo eliminado correctamente.\n";
} else {
    echo "Error al eliminar el archivo.\n";
}

//Dificultad Extra

// Nombre del archivo donde se almacenarán las ventas
$archivoVentas = "ventas.txt";

// Función para mostrar el menú
function mostrarMenu() {
    echo "\nGestión de Ventas:\n";
    echo "1. Añadir producto\n";
    echo "2. Consultar productos\n";
    echo "3. Actualizar producto\n";
    echo "4. Eliminar producto\n";
    echo "5. Calcular venta total\n";
    echo "6. Calcular venta por producto\n";
    echo "7. Salir\n";
    echo "Seleccione una opción: ";
}

// Función para añadir un producto
function agregarProducto() {
    global $archivoVentas;
    echo "Ingrese el nombre del producto: ";
    $nombre = trim(fgets(STDIN));
    echo "Ingrese la cantidad vendida: ";
    $cantidad = trim(fgets(STDIN));
    echo "Ingrese el precio: ";
    $precio = trim(fgets(STDIN));
    file_put_contents($archivoVentas, "$nombre, $cantidad, $precio\n", FILE_APPEND);
    echo "Producto añadido correctamente.\n";
}

// Función para consultar productos
function consultarProductos() {
    global $archivoVentas;
    if (file_exists($archivoVentas)) {
        echo "\nListado de productos:\n" . file_get_contents($archivoVentas);
    } else {
        echo "No hay productos registrados.\n";
    }
}

// Función para actualizar un producto
function actualizarProducto() {
    global $archivoVentas;
    if (!file_exists($archivoVentas)) {
        echo "No hay productos registrados.\n";
        return;
    }
    echo "Ingrese el nombre del producto a actualizar: ";
    $nombreActualizar = trim(fgets(STDIN));
    $lineas = file($archivoVentas, FILE_IGNORE_NEW_LINES);
    $nuevasLineas = [];
    $encontrado = false;
    foreach ($lineas as $linea) {
        list($nombre, $cantidad, $precio) = explode(", ", $linea);
        if ($nombre === $nombreActualizar) {
            echo "Ingrese la nueva cantidad: ";
            $cantidad = trim(fgets(STDIN));
            echo "Ingrese el nuevo precio: ";
            $precio = trim(fgets(STDIN));
            $nuevasLineas[] = "$nombre, $cantidad, $precio";
            $encontrado = true;
        } else {
            $nuevasLineas[] = $linea;
        }
    }
    if ($encontrado) {
        file_put_contents($archivoVentas, implode("\n", $nuevasLineas) . "\n");
        echo "Producto actualizado correctamente.\n";
    } else {
        echo "Producto no encontrado.\n";
    }
}

// Función para eliminar un producto
function eliminarProducto() {
    global $archivoVentas;
    if (!file_exists($archivoVentas)) {
        echo "No hay productos registrados.\n";
        return;
    }
    echo "Ingrese el nombre del producto a eliminar: ";
    $nombreEliminar = trim(fgets(STDIN));
    $lineas = file($archivoVentas, FILE_IGNORE_NEW_LINES);
    $nuevasLineas = [];
    foreach ($lineas as $linea) {
        list($nombre, $cantidad, $precio) = explode(", ", $linea);
        if ($nombre !== $nombreEliminar) {
            $nuevasLineas[] = $linea;
        }
    }
    file_put_contents($archivoVentas, implode("\n", $nuevasLineas) . "\n");
    echo "Producto eliminado correctamente.\n";
}

// Función para calcular la venta total
function calcularVentaTotal() {
    global $archivoVentas;
    if (!file_exists($archivoVentas)) {
        echo "No hay productos registrados.\n";
        return;
    }
    $total = 0;
    foreach (file($archivoVentas, FILE_IGNORE_NEW_LINES) as $linea) {
        list($nombre, $cantidad, $precio) = explode(", ", $linea);
        $total += $cantidad * $precio;
    }
    echo "Venta total: $total\n";
}

// Función para calcular la venta por producto
function calcularVentaPorProducto() {
    global $archivoVentas;
    if (!file_exists($archivoVentas)) {
        echo "No hay productos registrados.\n";
        return;
    }
    echo "Ingrese el nombre del producto: ";
    $nombreBuscar = trim(fgets(STDIN));
    foreach (file($archivoVentas, FILE_IGNORE_NEW_LINES) as $linea) {
        list($nombre, $cantidad, $precio) = explode(", ", $linea);
        if ($nombre === $nombreBuscar) {
            echo "Venta total de $nombre: " . ($cantidad * $precio) . "\n";
            return;
        }
    }
    echo "Producto no encontrado.\n";
}

// Bucle principal del menú
while (true) {
    mostrarMenu();
    $opcion = trim(fgets(STDIN));
    switch ($opcion) {
        case "1": agregarProducto(); break;
        case "2": consultarProductos(); break;
        case "3": actualizarProducto(); break;
        case "4": eliminarProducto(); break;
        case "5": calcularVentaTotal(); break;
        case "6": calcularVentaPorProducto(); break;
        case "7":
            unlink($archivoVentas);
            echo "Archivo de ventas eliminado. Saliendo...\n";
            exit();
        default:
            echo "Opción no válida. Intente de nuevo.\n";
    }
}


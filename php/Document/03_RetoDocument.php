<?php

// Arreglo normal (indexado numéricamente)
$numeros = [10, 20, 30, 40];

// Arreglo asociativo
$persona = [
    "nombre" => "Juan",
    "edad" => 25,
    "ciudad" => "Madrid"
];

// Acceder a valores
echo $numeros[1]; // 20
echo $persona["nombre"]; // Juan

/************************************************************************************************************* */

// Agregar un elemento (al final)
$numeros[] = 50; 

// Agregar un elemento en una posición específica
$numeros[2] = 100; // Reemplaza el valor en la posición 2

// Eliminar un elemento (unset no reordena los índices)
unset($numeros[1]); 

// Buscar un elemento con isset (para verificar si existe en un índice específico)
if (isset($numeros[2])) {
    echo "El índice 2 existe y su valor es: " . $numeros[2] . "\n";
} else {
    echo "El índice 2 no existe.\n";
}

// Buscar un valor con in_array (para verificar si existe el valor en el array)
if (in_array(100, $numeros)) {
    echo "El valor 100 está en el arreglo.\n";
} else {
    echo "El valor 100 no está en el arreglo.\n";
}

// Mostrar el arreglo
print_r($numeros);

/***************************************************************************************************************************** */
// Crear un arreglo asociativo
$persona = [
    "nombre" => "Juan",
    "edad" => 25,
    "ciudad" => "Madrid"
];

// Agregar un nuevo valor
$persona["profesion"] = "Ingeniero";

// Actualizar un valor existente
$persona["edad"] = 26; 

// Eliminar un valor
unset($persona["ciudad"]);

// Buscar una clave con isset (para verificar si existe una clave específica)
if (isset($persona["nombre"])) {
    echo "El nombre es: " . $persona["nombre"] . "\n";
} else {
    echo "La clave 'nombre' no existe.\n";
}

// Buscar un valor con in_array (para verificar si existe el valor en el array)
if (in_array("Ingeniero", $persona)) {
    echo "El valor 'Ingeniero' está en el arreglo.\n";
    // Mostrar el arreglo
    print_r($persona);
} else {
    echo "El valor 'Ingeniero' no está en el arreglo.\n";
}


/*************************************** */

// Arreglo asociativo de contactos
$contactos = [
    "Juan" => "juan@email.com",
    "Maria" => "maria@email.com",
    "Pedro" => "pedro@email.com"
];

$nombreModificar = "Maria"; // Clave actual
$nuevoNombre = "Mariana";   // Nueva clave

// Verificar si el contacto existe antes de renombrarlo
if (isset($contactos[$nombreModificar])) {
    // Copiar el valor a la nueva clave
    $contactos[$nuevoNombre] = $contactos[$nombreModificar]; 
    // Eliminar la clave antigua
    unset($contactos[$nombreModificar]);

    echo "Nombre cambiado exitosamente.\n";
} else {
    echo "El contacto no existe.\n";
}

// Mostrar el array actualizado
print_r($contactos);


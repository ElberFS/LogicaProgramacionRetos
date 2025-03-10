<?php
/*

 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

#arreglo que contendra los contactos
$contactos  = [];

#menu de opciones

function menu(){
    echo "\n--- Menú de Opciones ---\n";
    echo "1. Busqueda\n";
    echo "2. Inserción\n";
    echo "3. Actualización\n";
    echo "4. Eliminación\n";
    echo "5. Mostrar Contactos\n";
    echo "6. Salir\n";
}
while(true){
    menu();
    echo "Selecionar un opción: ";
    $opcion = intval(trim(fgets(STDIN)));    
    /*
    fgets(STDIN)
        fgets() lee una línea de entrada desde el teclado (entrada estándar STDIN).
        Espera a que el usuario ingrese un valor y presione "Enter".
        Devuelve la cadena ingresada, incluyendo el salto de línea (\n).
    trim(fgets(STDIN))
        trim() elimina los espacios en blanco al inicio y al final de la cadena, incluyendo el salto de línea (\n).
        Sin trim(), la cadena podría tener caracteres no deseados.
    intval(trim(fgets(STDIN)))
        intval() convierte la cadena limpia en un número entero.
        Si el usuario ingresa un valor no numérico, intval() devuelve 0.
    */
    switch ($opcion) {
        case 1:
            buscar_contacto();
            break;
        case 2:
            agregar_contacto();
            break;
        case 3:
            actualizar_contacto();
            break;
        case 4:
            eliminar_contacto();
            break;
        case 5:
            mostrar_contactos();
            break;
        case 6:
            echo "Saliendo...\n";
        exit;
        default:
            echo "Opción no válida.\n";
    }
}



function buscar_contacto(){
    global $contactos;
    echo "Ingrese el nombre a buscar: ";
    $contacto_buscar = trim(fgets(STDIN));
    $contacto_buscar = strtolower($contacto_buscar);
    #verificamos si la variable existe  en el arreglo
    if(isset($contactos[$contacto_buscar])){
        echo "Numero de $contacto_buscar: " .$contactos[$contacto_buscar];
    } else {
        echo "Contacto no encontrado.\n";
    }
}
function agregar_contacto(){
    global $contactos;
    echo "Ingresar el Nombre ";
    $nombre_contacto = trim(fgets(STDIN));
    $nombre_contacto = strtolower($nombre_contacto); 
    echo "Ingrese el Numero Celular ";
    $numero_contacto = intval(trim(fgets(STDIN)));
    #creamos un arreglo asosiativo
    $contactos[$nombre_contacto] = $numero_contacto;
    echo "Contacto Agregado con exito";
}
function actualizar_contacto(){
    global $contactos;
    echo "Ingresar el nombre del contacto que desea actualizar: ";
    $contacto_modificar = trim(fgets(STDIN));
    $contacto_modificar =strtolower($contacto_modificar); 
    //Menu para eligir que dato se va a modificar
        if(isset($contactos[$contacto_modificar])){
            echo "\n--- Opciones de actualización ---\n";
                    echo "1. Modificar solo el nombre\n";
                    echo "2. Modificar solo el número\n";
                    echo "3. Salir\n";
                    echo "Seleccione una opción: ";

        $opcion_actualizar = intval(trim(fgets(STDIN)));
        switch ($opcion_actualizar){
            case 1:
                echo "Ingrese el nuevo nombre";
                $nuevo_nombre = trim(fgets(STDIN));
                $nuevo_nombre = strtolower($nuevo_nombre); 
                /*
                copiamos el valos a la nueva clave es decir asociamos 
                el numero con nuevo nombre del contacto 
                ejemplo si 
                juan - 123
                el nuevo contacto pedro tambien se le asociara :
                pedro - 123 
                */
                $contactos[$nuevo_nombre] = $contactos[$contacto_modificar];
                //eliminamos el contacto antiguo usando unset
                unset($contactos[$contacto_modificar]);
                echo "Nombre actualizado correctamente.\n";
                break;
            case 2:
                echo "Ingrese el nuevo número: ";
                        $nuevo_numero = intval(trim(fgets(STDIN)));

                        $contactos[$contacto_modificar] = $nuevo_numero;
                        echo "Número actualizado correctamente.\n";
                break;
            case 3:
                echo "Saliendo...\n";
            exit;
            default:
                echo "Opción no válida.\n"; 
        }
    }
}
function eliminar_contacto(){
    global $contactos;
    echo "Ingrese el nombre del contacto que desea eliminar: ";
    $contacto_eliminar  = trim(fgets(STDIN));
    $contacto_eliminar = strtolower($contacto_eliminar);
    if (isset($contactos[$contacto_eliminar])) {
        unset($contactos[$contacto_eliminar]);
        echo "Contacto eliminado correctamente.\n";
    } else {
        echo "Contacto no encontrado.\n";
    }
}

function mostrar_contactos() {
    global $contactos;

    if (empty($contactos)) {
        echo "La agenda está vacía.\n";
    } else {
        echo "\n--- Lista de Contactos ---\n";
        foreach ($contactos as $nombre => $numero) {
            echo "Nombre: $nombre - Número: $numero\n";
        }
    }
}

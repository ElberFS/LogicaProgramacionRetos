<?php 
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
 */



class Persona {
    /**
      * Clase que representa a una persona con nombre, edad y ciudad.
      */
    private string $nombre;
    private int $edad;
    private string $ciudad;

    /**
      * Constructor de la clase Persona.
      * @param string $nombre Nombre de la persona
      * @param int $edad Edad de la persona
      * @param string $ciudad Ciudad de residencia de la persona
      */
    public function __construct(string $nombre, int $edad, string $ciudad) {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->ciudad = $ciudad;
    }

    /**
      * Método para mostrar la información de la persona.
      */
    public function mostrarInformacion(): void {
        echo "Nombre: {$this->nombre}, Edad: {$this->edad}, Ciudad: {$this->ciudad}\n";
    }

    /**
      * Métodos para modificar los atributos.
      */
    public function setNombre(string $nombre): void {
        $this->nombre = $nombre;
    }

    public function setEdad(int $edad): void {
        $this->edad = $edad;
    }

    public function setCiudad(string $ciudad): void {
        $this->ciudad = $ciudad;
    }
}

 // Creación de una instancia de la clase Persona
$persona1 = new Persona("Carlos Pérez", 30, "Lima");

 // Mostrar información inicial
echo "Información inicial:\n";
$persona1->mostrarInformacion();

 // Modificación de atributos
$persona1->setNombre("Ana Gómez");
$persona1->setEdad(25);
$persona1->setCiudad("Bogotá");

 // Mostrar información actualizada
echo "\nInformación actualizada:\n";
$persona1->mostrarInformacion();


/*** Dificultad extra **** */


class Pila {
    private array $elementos;

    public function __construct() {
        $this->elementos = [];
    }

    public function apilar($elemento): void {
        array_push($this->elementos, $elemento);
    }

    public function desapilar() {
        return empty($this->elementos) ? null : array_pop($this->elementos);
    }

    public function tamano(): int {
        return count($this->elementos);
    }

    public function mostrar(): void {
        echo "Contenido de la pila: " . implode(", ", array_reverse($this->elementos)) . "\n";
    }
}

class Cola {
    private array $elementos;

    public function __construct() {
        $this->elementos = [];
    }

    public function encolar($elemento): void {
        array_push($this->elementos, $elemento);
    }

    public function desencolar() {
        return empty($this->elementos) ? null : array_shift($this->elementos);
    }

    public function tamano(): int {
        return count($this->elementos);
    }

    public function mostrar(): void {
        echo "Contenido de la cola: " . implode(", ", $this->elementos) . "\n";
    }
}

// Pruebas con la Pila
echo "--- Pila ---\n";
$pila = new Pila();
$pila->apilar("A");
$pila->apilar("B");
$pila->apilar("C");
$pila->mostrar();
echo "Elemento desapilado: " . $pila->desapilar() . "\n";
$pila->mostrar();

echo "\n--- Cola ---\n";
// Pruebas con la Cola
$cola = new Cola();
$cola->encolar("1");
$cola->encolar("2");
$cola->encolar("3");
$cola->mostrar();
echo "Elemento desencolado: " . $cola->desencolar() . "\n";
$cola->mostrar();


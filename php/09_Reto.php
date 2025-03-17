<?php
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 */


// Creacion de la Super clase Animal
class Animal {
    protected string $nombre;
    protected string $sonido;

    public function __construct(string $nombre, string $sonido) {
        $this->nombre = $nombre;
        $this->sonido = $sonido;
    }

    //Metodo que muestra el sonido del animal
    public  function SonidoAnima(){
        echo "El anima {$this->nombre} hace {$this->sonido}\n";
    }
}

// Creacion de la subclase Perro
class Perro extends Animal {
    public function __construct(string $nombre) {
        parent::__construct($nombre, "guau");
        $this->nombre = $nombre;
    }

    //Metodo que muestra el sonido del perro
    public function SonidoPerro(){
        echo "El perro {$this->nombre} hace {$this->sonido}\n";
    }
}

// Creacion de la subclase Gato
class Gato extends Animal {
    public function __construct(string $nombre) {
        parent::__construct($nombre, "miau");
        $this->nombre = $nombre;
    }

    //Metodo que muestra el sonido del gato
    public function SonidoGato(){
        echo "El gato {$this->nombre} hace {$this->sonido}\n";
    }
}

//ejemplo de uso

$perro = new Perro("Firulais");
$gato = new Gato("Garfield");
echo $perro->SonidoPerro();
echo $gato->SonidoGato();

//Dificultad extra

// Superclase Empleado que representa a cualquier trabajador de la empresa
class Empleado {
    protected int $id;
    protected string $nombre;
    protected string $cargo;

    public function __construct(int $id, string $nombre, string $cargo) {
        $this->id = $id;
        $this->nombre = $nombre;
        $this->cargo = $cargo;
    }

    public function obtenerInformacion(): string {
        return "Empleado: {$this->nombre} ({$this->cargo}), ID: {$this->id}";
    }
}

// Subclase Gerente
class Gerente extends Empleado {
    private array $empleadosACargo = [];

    public function __construct(int $id, string $nombre) {
        parent::__construct($id, $nombre, "Gerente");
    }

    public function agregarEmpleado(Empleado $empleado): void {
        $this->empleadosACargo[] = $empleado;
    }

    public function listarEmpleados(): void {
        echo "\nEmpleados a cargo de {$this->nombre}:\n";
        foreach ($this->empleadosACargo as $empleado) {
            echo " - " . $empleado->obtenerInformacion() . "\n";
        }
    }
}

// Subclase Gerente de Proyectos
class GerenteDeProyectos extends Empleado {
    private string $proyecto;

    public function __construct(int $id, string $nombre, string $proyecto) {
        parent::__construct($id, $nombre, "Gerente de Proyectos");
        $this->proyecto = $proyecto;
    }

    public function obtenerProyecto(): string {
        return "El gerente de proyectos {$this->nombre} está a cargo del proyecto: {$this->proyecto}.";
    }
}

// Subclase Programador
class Programador extends Empleado {
    private string $lenguaje;

    public function __construct(int $id, string $nombre, string $lenguaje) {
        parent::__construct($id, $nombre, "Programador");
        $this->lenguaje = $lenguaje;
    }

    public function obtenerLenguaje(): string {
        return "El programador {$this->nombre} domina el lenguaje: {$this->lenguaje}.";
    }
}

// Ejemplo de uso
$gerente = new Gerente(1, "Carlos Pérez");
$gerenteProyecto = new GerenteDeProyectos(2, "Ana López", "Sistema de Facturación");
$programador1 = new Programador(3, "Juan Ramírez", "PHP");
$programador2 = new Programador(4, "Laura Gómez", "JavaScript");

// Asignamos programadores al gerente
$gerente->agregarEmpleado($gerenteProyecto);
$gerente->agregarEmpleado($programador1);
$gerente->agregarEmpleado($programador2);

// Mostrar información
echo $gerente->obtenerInformacion() . "\n";
$gerente->listarEmpleados();

echo "\n" . $gerenteProyecto->obtenerProyecto() . "\n";

echo "\n" . $programador1->obtenerLenguaje() . "\n";
echo $programador2->obtenerLenguaje() . "\n";

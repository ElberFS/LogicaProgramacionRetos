<?php
/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

/**
 * Clase Stack (Pila - LIFO)
 * Implementa una pila con operaciones básicas.
 */


/***************
 * Clase Stack (Pila - LIFO)
 ***************/
class Stack {
    private array $stack = [];
    
    public function push(string $item): void {
        $this->stack[] = $item;
    }
    
    public function pop(): ?string {
        return array_pop($this->stack);
    }
    
    public function peek(): ?string {
        return end($this->stack) ?: null;
    }
}

/***************
 * Clase Queue (Cola - FIFO)
 ***************/
class Queue {
    private array $queue = [];
    
    public function enqueue(string $item): void {
        $this->queue[] = $item;
    }
    
    public function dequeue(): ?string {
        return array_shift($this->queue);
    }
    
    public function isEmpty(): bool {
        return empty($this->queue);
    }
}

/***************/ // dificultad extra
/***************
 * Simulación del mecanismo Adelante/Atrás de un navegador web
 ***************/
class BrowserNavigation {
    private Stack $backStack;
    private Stack $forwardStack;
    private ?string $currentPage = null;
    
    public function __construct() {
        $this->backStack = new Stack();
        $this->forwardStack = new Stack();
    }
    
    public function visit(string $page): void {
        if ($this->currentPage !== null) {
            $this->backStack->push($this->currentPage);
        }
        $this->currentPage = $page;
        $this->forwardStack = new Stack(); // Limpiar historial de adelante
        echo "Visitando: $page\n";
    }
    
    public function back(): void {
        if ($previous = $this->backStack->pop()) {
            $this->forwardStack->push($this->currentPage);
            $this->currentPage = $previous;
            echo "Retrocediendo a: $previous\n";
        } else {
            echo "No hay páginas anteriores.\n";
        }
    }
    
    public function forward(): void {
        if ($next = $this->forwardStack->pop()) {
            $this->backStack->push($this->currentPage);
            $this->currentPage = $next;
            echo "Avanzando a: $next\n";
        } else {
            echo "No hay páginas siguientes.\n";
        }
    }
}

/***************/ // dificultad extra
/***************
 * Simulación de una impresora con una cola de impresión
 ***************/
class PrinterQueue {
    private Queue $printQueue;
    
    public function __construct() {
        $this->printQueue = new Queue();
    }
    
    public function addDocument(string $document): void {
        $this->printQueue->enqueue($document);
        echo "Documento agregado a la cola: $document\n";
    }
    
    public function printDocument(): void {
        if ($document = $this->printQueue->dequeue()) {
            echo "Imprimiendo documento: $document\n";
        } else {
            echo "No hay documentos en la cola de impresión.\n";
        }
    }
}

/***************
 * Simulación del navegador web
 ***************/
$browser = new BrowserNavigation();
$browser->visit("google.com");
$browser->visit("github.com");
$browser->visit("stackoverflow.com");
$browser->back();
$browser->back();
$browser->forward();

/***************
 * Simulación de la impresora
 ***************/
$printer = new PrinterQueue();
$printer->addDocument("Informe.pdf");
$printer->addDocument("Presentación.pptx");
$printer->printDocument();
$printer->printDocument();
$printer->printDocument();

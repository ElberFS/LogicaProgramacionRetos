<?php 

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han
 *   finalizado.
 */


/**
 * Función para ejecutar una tarea asíncrona en Windows.
 *
 * @param string $nombre Nombre de la tarea.
 * @param int $segundos Tiempo de ejecución en segundos.
 */
function ejecutarTareaAsincrona(string $nombre, int $segundos) {
    echo "🔄 Tarea '$nombre' iniciada. Durará $segundos segundos.\n";
    
    // Ejecutar en segundo plano en Windows
    if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
        pclose(popen("start /B php -r \"sleep($segundos); echo '✅ Tarea \'$nombre\' finalizada.\\n';\"", "r"));
    } else {
        exec("php -r \"sleep($segundos); echo '✅ Tarea \'$nombre\' finalizada.\\n';\" > /dev/null 2>&1 &");
    }
}

// Ejecutar tareas en paralelo (C, B, A)
ejecutarTareaAsincrona("C", 3);
ejecutarTareaAsincrona("B", 2);
ejecutarTareaAsincrona("A", 1);

// Esperar a que terminen todas antes de ejecutar D
sleep(4);
echo "🔄 Tarea 'D' iniciada. Durará 1 segundo.\n";
sleep(1);
echo "✅ Tarea 'D' finalizada.\n";

echo "🛑 Todas las tareas han finalizado.\n";

// ---- DIFICULTAD EXTRA ----

/**
 * Función para ejecutar una tarea con espera controlada.
 *
 * @param string $nombre Nombre de la tarea.
 * @param int $segundos Tiempo de ejecución en segundos.
 */
function ejecutarTarea(string $nombre, int $segundos) {
    echo "🔄 Tarea '$nombre' iniciada. Durará $segundos segundos.\n";
    sleep($segundos); // Simula la ejecución
    echo "✅ Tarea '$nombre' finalizada.\n";
}

// Ejecutar tareas en paralelo con exec()
exec("start /B php -r \"sleep(3); echo '✅ Tarea C finalizada.\\n';\"");
exec("start /B php -r \"sleep(2); echo '✅ Tarea B finalizada.\\n';\"");
exec("start /B php -r \"sleep(1); echo '✅ Tarea A finalizada.\\n';\"");

// Esperar lo suficiente para que todas terminen antes de ejecutar D
sleep(4);

// Ejecutar D después de que C, B y A hayan terminado
ejecutarTarea("D", 1);

echo "🛑 Todas las tareas han finalizado.\n";

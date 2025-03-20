<?php 

/*
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
 */


 // Fecha actual
$fechaActual = new DateTime();

// Fecha de nacimiento (modifica con tu fecha real)
$fechaNacimiento = new DateTime("1999-03-15 10:30:00");

// Calcular la diferencia
$diferencia = $fechaNacimiento->diff($fechaActual);

// Mostrar los años transcurridos
echo "Han transcurrido " . $diferencia->y . " años.";

// DIFICULTAD EXTRA (opcional)
// Crear objeto DateTime con tu fecha de nacimiento
$fechaCumple = new DateTime("2001-11-09 14:45:30"); 

// Diferentes formatos
$formato1 = $fechaCumple->format("d/m/Y"); // Día, mes y año
$formato2 = $fechaCumple->format("H:i:s"); // Hora, minuto y segundo
$formato3 = $fechaCumple->format("z"); // Día del año (0-365)
$formato4 = $fechaCumple->format("l"); // Día de la semana (en inglés)
$formato5 = $fechaCumple->format("F"); // Nombre del mes (en inglés)
$formato6 = $fechaCumple->format("Y-m-d H:i"); // Formato completo sin segundos
$formato7 = $fechaCumple->format("dS \of F, Y"); // Día con sufijo (como "9th of November, 2001")
$formato8 = $fechaCumple->format("W"); // Número de la semana del año
$formato9 = $fechaCumple->format("D, M j, Y"); // Formato corto tipo "Fri, Nov 9, 2001"
$formato10 = $fechaCumple->format("h:i A"); // Hora en formato 12 horas con AM/PM

// Mostrar resultados
echo "1 Día, mes y año : $formato1\n";
echo "2 Hora, minuto y segundo : $formato2\n";
echo "3 Día del año : $formato3\n";
echo "4 Día de la semana : $formato4\n";
echo "5 Nombre del mes : $formato5\n";
echo "6 Formato completo : $formato6\n";
echo "7 Día con sufijo y mes : $formato7\n";
echo "8 Número de la semana del año : $formato8\n";
echo "9 Formato corto tipo email : $formato9\n";
echo "10 Hora en formato 12h : $formato10\n";

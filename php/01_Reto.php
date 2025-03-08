<?php
/*
#01 OPERADORES Y ESTRUCTURAS DE CONTROL
    Crea un programa que imprima por consola todos los números 
    comprendidos entre 10 y 55 (incluidos), pares, y que no son
    ni el 16 ni múltiplos de 3
*/


for($i = 1 ; $i <=55 ; $i++){
    if($i>=10){
        if($i % 2 == 0  && $i != 16 ){
            if( ($i % 3) != 0 ){
                echo $i . "\n";
            }
        }    
    }    
}
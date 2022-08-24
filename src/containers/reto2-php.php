<?php
function reglafibonacci($pfibonacci){

    $primerNumero=1;
    $segundoNumero=1;
    if ($pfibonacci==1) {
        echo('0');hx
    }
    elseif ($pfibonacci==2) {
    	echo('0 1') ;
    	
    }
    else{
        echo('0');
        echo($primerNumero);
        echo($segundoNumero);
        for ( $numeros = 47; $numeros > 0;$numeros--){
            $total = $primerNumero + $segundoNumero;
            $segundoNumero=$primerNumero;
            $primerNumero= $total;
            echo($total);
        }
    }
}
reglafibonacci(50);
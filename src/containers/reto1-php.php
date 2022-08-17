<?php

function palabrasAnagrama (){
    $primeraPalabra = ["J", "A" , "P" , "O" , "N", "E", "S"];
    $primeraPalabrasort=$primeraPalabra.sort();
  	echo($primeraPalabra);
    $SegundaPalabra = ["E", "S", "P", "O", "N", "J", "A"];
    $segundaPalabrasort=$SegundaPalabra.sort();
  	echo($SegundaPalabra);
    return $primeraPalabrasort.toString() === $segundaPalabrasort.toString();

echo (palabrasAnagrama());
}
<?php
for ($numero=1; $numero < 101; $numero++){
    if ($numero%3 == 0 and $numero%5 == 0){
        echo ("fizzbuzz");}
    elseif($numero%3 == 0){
        echo("Fizz");}
	elseif($numero%5 == 0){
        echo("Buzz");}
    else {
        echo ($numero);}
}
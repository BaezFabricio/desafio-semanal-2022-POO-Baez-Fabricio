for (let numero=1; numero < 101; numero++){
    if (numero % 3 == 0 && numero % 5 == 0)
           console.log("fizzbuzz")
    else if (numero%3 == 0)
           console.log("Fizz")
    else if (numero%5 == 0)
           console.log("Buzz")
    else 
           console.log(numero)
   }
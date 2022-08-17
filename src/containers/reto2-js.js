function reglafibonacci(pfibonacci){

    let primerNumero=1
    let segundoNumero=1
    if (pfibonacci==1){
        console.log('0',)
    }
    else if (pfibonacci==2){
        console.log('0','1')
    }
    else{
        console.log('0')
        console.log(primerNumero)
        console.log(segundoNumero)
        for (var numeros = 47; numeros > 0; numeros--) {
            let total = primerNumero + segundoNumero
            segundoNumero=primerNumero
            primerNumero= total
            console.log(total)}
    }
}
reglafibonacci(50)
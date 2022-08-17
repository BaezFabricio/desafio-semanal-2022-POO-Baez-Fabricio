def reglafibonacci(pfibonacci):

    primerNumero=1
    segundoNumero=1
    if pfibonacci==1:
        print('0',)
    elif pfibonacci==2:
        print('0','1')
    else:
        print('0', end= "  ")
        print(primerNumero, end = "  ")
        print(segundoNumero, end = "  ")
        for numeros in range(pfibonacci-3):
            total = primerNumero + segundoNumero
            segundoNumero=primerNumero
            primerNumero= total
            print(total, end = "  ")
         
reglafibonacci(50)
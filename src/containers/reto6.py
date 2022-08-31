cadena = "Hola Mundo"
alReves=[]
cantIndex = len(cadena)
while cantIndex > 0: 
    alReves += cadena[cantIndex-1]
    cantIndex = cantIndex - 1 # decrement index
    imprimir = "".join(alReves)
print(imprimir)
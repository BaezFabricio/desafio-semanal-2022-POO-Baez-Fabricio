num= int(input("Ingrese un numero"))

def calculoPrimo (pnum):
    for numero in range(1, pnum):
        if pnum % numero ==0:
            print ("No es primo", numero)
            return False
        print ("Es primo")
        return True
print(calculoPrimo(num))
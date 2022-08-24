base= int(input("Ingrese el valor de base"))
altura= int(input("Ingrese el valor de la altura"))
tipoPoligono= str(input("Ingrese el tipo de poligono"))

def areaPoligono(pbase, paltura, ppoligono):
    if ppoligono== "triangulo"or ppoligono== "rectangulo"or ppoligono== "cuadrado":
    
        if ppoligono == "triangulo":
            area = (pbase * paltura/2)
            print(f"el area del {ppoligono} es: {area}")
        else:
            area= (pbase * paltura)
            print(f"el area del {ppoligono} es {area}")
    else:
        print("ha ingresado una figura geometrica incorrecta")

areaPoligono(base,altura,tipoPoligono)
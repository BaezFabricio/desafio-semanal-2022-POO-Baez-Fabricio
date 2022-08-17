from tkinter import N


for numeros in range (1,101):
    if numeros%3 == 0 and numeros%5 == 0:
        print ("fizzbuzz")
    elif (numeros%3 == 0):
        print("Fizz")
    elif (numeros%5 == 0):
        print("Buzz")
    else: 
        print (numeros)
import string

def palabrasAnagrama ():
    primeraPalabra = ["J", "A" , "P" , "O" , "N", "E", "S"]
    primeraPalabra.sort()
    SegundaPalabra = ["E", "S", "P", "O", "N", "J", "A"]
    SegundaPalabra.sort()
    return primeraPalabra == SegundaPalabra
print(palabrasAnagrama())

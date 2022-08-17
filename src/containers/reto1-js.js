function palabrasAnagrama (){
    let primeraPalabra = ["J", "A" , "P" , "O" , "N", "E", "S"]
    let primeraPalabrasort=primeraPalabra.sort()
  	console.log(primeraPalabra)
    let SegundaPalabra = ["E", "S", "P", "O", "N", "J", "A"]
    let segundaPalabrasort=SegundaPalabra.sort()
  	console.log(SegundaPalabra)
    return primeraPalabrasort.toString() === segundaPalabrasort.toString()
}
console.log(palabrasAnagrama())
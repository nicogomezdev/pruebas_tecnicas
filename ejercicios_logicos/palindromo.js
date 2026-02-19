let palabra ='anan';

function palindromo(palabra){
    let inverPalabra = palabra.split('').reverse().join('');
    console.log(inverPalabra)
    if(inverPalabra==palabra){
        console.log(`Es un palíndromo la palabra ${palabra}`)
    }else{
        console.log(`La palabra ${palabra} no es un palíndromo, ya que invertida es ${inverPalabra} y no cumple la condición de que al derecho y al reves sean iguales`)
    }

}

palindromo(palabra);
//buscar la palabra de tal frase y decir cuantas veces se repite
// la palabra y la frase deben ser parametros de una función

let frase='hola mi nombre es karina kfsjjsfkfs hbfjksf karina'
let palabra='Karina'
var contador=0;

function buscar(frase, palabra){
    var customizar= frase.toLowerCase().replace(/[!,.-]/gi,'');
    var customizarPalabra= palabra.toLowerCase();
    var array= customizar.split(' ');

    for (let i=0; i<array.length;i++){
        if (array[i]===customizarPalabra){
            contador++;
        }
    }
    console.log(`Se repite ${contador} veces`)
}

buscar(frase, palabra);
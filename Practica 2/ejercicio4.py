def cambiarLetra(cadena: str, letra: str, nuevaLetra: str) -> (str|None):
    
    pos = 0
    # Chequeo que la letra esta dentro de la cadena
    
    pos = cadena.find(letra)

    if(pos == -1):
        return "ERROR - No se encuentra la letra en la palabra!"

    # Reemplazo de la letra

    splitIzq = cadena[0:pos]
    splitDer = cadena[pos+1:]


    return splitIzq + nuevaLetra + splitDer

print(cambiarLetra("hola","c","a"))

palabra = "abac"

def eliminarItems(palabra: str,parametro: str) -> str:

    for i in palabra:
        if(i == parametro):
            palabra.remove(i) # Esto da error porque no se puede echar un item en una cadena ya que es inmutable

    return palabra

nuevapalabra = eliminarItems(palabra,"a") # Esto da error por lo mencionado anteriormente

print(nuevapalabra)
print("Coinciden los id: " + str((palabra == nuevapalabra))) # No van a coincidir aunque funcione mi def porque apuntaria a un nuevo espacio en la memoria
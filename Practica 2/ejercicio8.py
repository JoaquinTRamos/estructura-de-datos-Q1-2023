lista = ["a","b","a","c"]

def eliminarItems(lista: list[str],parametro: str) -> list[str]:

    for i in lista:
        if(i == parametro):
            lista.remove(i)

    return lista

nuevaLista = eliminarItems(lista,"a")

print(nuevaLista)
print("Coinciden los id: " + str((lista == nuevaLista))) # Coinciden porque una lista es MUTABLE, por lo tanto apuntan al mismo espacio de memoria

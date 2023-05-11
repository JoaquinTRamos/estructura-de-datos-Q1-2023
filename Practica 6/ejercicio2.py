from typing import TypeVar, Generic

T = TypeVar('T')

class NodoCola(Generic[T]):
    def __init__(self,item:T, posicion: int) -> None:
        self.item: T = item
        self.posicion: int = posicion

    def __str__(self) -> str:
        return f"item: {self.item}, posicion: {self.posicion}"

    def MoverAdelante(self) -> None:
        self.posicion -= 1

    def MoverAtras(self) -> None:
        self.posicion += 1


class Cola(Generic[T]):
    def __init__(self) -> None:
        self.nodos: list[NodoCola] = []
        self.totalnodos: int = 0
        self.items = self.__getItems()
        pass

    def __len__(self) -> int:
        return self.totalnodos

    def encolar(self, item:T):
        self.nodos.append(NodoCola(item,self.totalnodos))
        self.totalnodos += 1
        self.items = self.__getItems()
        pass

    def desencolar(self) -> T:
        nodoDescolado = self.nodos.pop(0)
        for nodo in self.nodos:
            nodo.MoverAdelante()
        self.totalnodos -= 1
        return nodoDescolado.item

    def vaciar(self) -> None:
        return self.nodos.clear()
    
    def dentro(self, item:T) -> bool:
        for nodo in self.nodos:
            if(item == nodo.item):
                return True
        
        return False
    
    def __getItems(self):
        resultado: list[T] = []
        for nodo in self.nodos:
            resultado.append(nodo.item)

        return tuple(resultado)
 
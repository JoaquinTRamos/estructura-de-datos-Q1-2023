class Album:
    def __init__(self) -> None:
        self.canciones = []

    def dameCancion(self,index:int) -> str:
        return self.canciones[index]
    
    def agregarCancion(self,cancion:str) -> None:
        self.canciones.append(cancion)

    def eliminarCancion(self, index: int) -> None:
        self.canciones.pop(index)

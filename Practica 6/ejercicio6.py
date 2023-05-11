import ejercicio2

class Ejercicio():
    def __init__(self, listaNum: list[int]) -> None:
        self.cola = self.crearCola(listaNum)
        self.resultado: list[int] = []
        self.procesar()

    def crearCola(self, listaNum: list[int]) -> ejercicio2.Cola[int]:
        resultado: ejercicio2.Cola[int] = ejercicio2.Cola()
        for i in listaNum:
            resultado.encolar(i)
        
        return resultado

    def procesar(self):
        currentList = []
        maxIndex = len(self.cola)
        i = 0
        n = 0
        m = 0 # n - 1
        while i < maxIndex:
            
            #Si no hay cola crear una y hacer que n - 1 = valor
            if len(currentList) == 0:
                m = self.cola.desencolar()
                currentList.append(m)
                i += 1
                continue

            n = self.cola.desencolar()
            
            #Si n = valor(n - 1) + 1 entonces agregar a la cola
            if n == (m + 1): 
                currentList.append(n)
            #Si n != valor(n - 1) + 1 entonces borrar cola y arrancar denuevo
            else:
                currentList.clear()
                currentList.append(n)

            m = n
            i += 1

        self.resultado = currentList

    def darResultado(self):
        return self.resultado


lista = [1,2,3,5,6,7,8,9]
ejercicio = Ejercicio(lista)
print(f"{lista} la sublista mas larga es {ejercicio.darResultado()}")
    
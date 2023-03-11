import random

class Examen:

    def __init__(self) -> None:
        self.notaTeorica = 0
        self.notaPractica = 0
        pass


class Person:

    def __init__(self, dni: int, codEmpleado: str, tipoLicencia: str, numTramite: str):
        self.dni = dni
        self.codEmpleado = codEmpleado
        self.tipoLicencia = tipoLicencia
        self.numeroTramite = numTramite
        self.examen = Examen()

    def Rendir(self):
        self.examen.notaTeorica = random.randint(0, 100)
        self.examen.notaPractica = random.randint(0, 100)
        pass      

    def VerificarExamen(self) -> bool:
        respuesta = self.examen.notaTeorica + self.examen.notaPractica / 2
        if(respuesta > 70):
            return True
        else:
            return False


def validarDNI(dni: str) -> bool:
    if(len(str(dni)) == 8 and dni.isnumeric()):
        return True
    else:
        return False

def validarCodEmpleado(codEmpleado: str) -> bool:
    if(len(codEmpleado) != 5):
        return False

    parteLetras = codEmpleado[0:3]
    parteNumeros = codEmpleado[3:5]

    if(parteLetras.isalpha() == False):
        return False
    if(parteNumeros.isnumeric() == False):
        return False
    
    return True
    
def validarTipoLicencia(codEmpleado: str) -> bool:
    if(codEmpleado == "PRO" or codEmpleado == "PAR"):
        return True
    else:
        return False

listaPersonas = []

def encontrarPorDNI(dni: int) -> (Person|None):
    for persona in listaPersonas:
        if(persona.dni == dni):
            return persona
    pass

def encontrarPorTramite(numTramite: str) -> (Person|None):
    for persona in listaPersonas:
        if(persona.numeroTramite == numTramite):
            return persona
    pass

def respuestaAB() -> (Person | None):
    print("A. Por DNI")
    print("B. Por Tramite")
    respuestaAB = str.upper(input("Ingrese opcion: "))
    match respuestaAB:
                case "A":
                    dni = input("Ingrese DNI: ")
                    if(validarDNI(dni) == False):
                        print("DNI invalido")
                        pass

                    # Busca dni en listaPersonas, si no existe volver a menu principal, si existe instancia = resultadoBusqueda
                    resultadoBusqueda = encontrarPorDNI(int(dni))

                    if(resultadoBusqueda is None):
                        print("No se encuentra registrado")
                        pass
                    else:
                        return resultadoBusqueda 
                case "B":
                    numTramite = input("Ingrese numero de tramite: ")

                    # Busca tramite en listaPersonas, si no existe volver a menu principal, si existe instancia = resultadoBusqueda
                    resultadoBusqueda = encontrarPorTramite(numTramite)

                    if(resultadoBusqueda is None):
                        print("No se encuentra registrado")
                        pass
                    else:
                        return resultadoBusqueda 
                case _:
                    print("Opcion invalida")
                    pass

while True:
    print("")
    print("Sistema de Registro Automotor")
    print("-----------------------------")
    print("1. Registro")
    print("2. Examen")
    print("3. Verificacion")
    print("4. Salir")

    respuesta = input("Ingrese opcion: ")

    match respuesta:
        case "1": # Registro
            dni: str = ""
            codEmpleado: str = ""
            tipoLicencia: str = ""
            numTramite: str = ""

            dni = input("Ingrese DNI: ")
            
            if(validarDNI(dni) == False):
                print("DNI invalido")
                continue
            
            codEmpleado = input("Ingrese codigo de empleado: ")
            if(validarCodEmpleado(codEmpleado) == False):
                print("Codigo de empleado invalido")
                continue
            
            
            tipoLicencia = input("Ingrese tipo de licencia: ")
            if(validarTipoLicencia(tipoLicencia) == False):
                print("Tipo de licencia invalido")
                continue

            numTramite = dni + codEmpleado + tipoLicencia

            print("Numero de tramite: " + numTramite)
            # Verificar que no exista en listaPersonas, si existe realizar caso 1 denuevo
            listaPersonas.append(Person(int(dni), codEmpleado, tipoLicencia, numTramite))

        case "2": # Examen
            resultadoAB = respuestaAB()
            
            if(resultadoAB is None):
                continue
            else:
                instancia = resultadoAB
            
            if(instancia.examen.notaTeorica < 10 or instancia.examen.notaPractica < 10):
                instancia.Rendir()
            
            print("Rindio el examen")
            print(str(instancia.examen.notaTeorica) + " y " + str(instancia.examen.notaPractica))


        case "3": # Verificacion
            resultadoAB = respuestaAB()
            
            if(resultadoAB is None):
                continue
            else:
                instancia = resultadoAB
            
            if(instancia.VerificarExamen()):
                print("Obtuvo el registro")
            else:
                print("No obtuvo el registro")

        case "4": # Salir
            break
        case _:
            print("Es inválida")
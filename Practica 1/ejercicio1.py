import random

class Examen:
    notaTeorica = random.randint(10,100)
    notaPractica = random.randint(10,100)

class Person:

    examen: Examen

    def __init__(self, dni: int, codEmpleado: str, tipoLicencia: str, numTramite: str):
        self.dni = dni
        self.codEmpleado = codEmpleado
        self.tipoLicencia = tipoLicencia
        self.numeroTramite = numTramite

    def Rendir(self):
        examen = Examen()
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

def encontrarPorTramite(numTramite: str):
    for persona in listaPersonas:
        if(persona.numTramite == numTramite):
            return persona
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
            print("A. Por DNI")
            print("B. Por Tramite")
            respuestaAB = input("Ingrese opcion: ")
            instancia: Person
            match respuestaAB:
                case "A":
                    dni = input("Ingrese DNI: ")
                    if(validarDNI(dni) == False):
                        print("DNI invalido")
                        continue

                    if(encontrarPorDNI(int(dni)) == None):
                        print("No se encuentra registrado")
                        continue
                    else:
                        instancia =  encontrarPorDNI(int(dni)) #Buscar como hacer que Python sepa que es de tipo Person
                case "B":
                    numTramite = input("Ingrese numero de tramite: ")
                    # Buscar numTramite en listaPersonas, si no existe volver a menu principal
                    instancia = listaPersonas[0] # CAMBIAR
                case _:
                    print("Opcion invalida")
                    continue

            if(instancia.examen == None): # Error temporal, esto aparece solo porque aun no escribi todo el codigo
                instancia.Rendir()
            
            print("Rindio el examen")
            print(str(instancia.examen.notaTeorica) + "y" + str(instancia.examen.notaPractica))


        # case "3": # Verificacion
        #     print("A. Por DNI")
        #     print("B. Por Tramite")
        #     respuestaAB = input("Ingrese opcion: ")
        #     instancia: Person
        #     match respuestaAB:
        #         case "A":
        #             dni = int(input("Ingrese DNI: "))
        #             # Buscar dni en listaPersonas, si no existe volver a menu principal
        #             instancia = listaPersonas[0] # CAMBIAR
        #         case "B":
        #             numTramite = input("Ingrese numero de tramite: ")
        #             # Buscar numTramite en listaPersonas, si no existe volver a menu principal
        #             instancia = listaPersonas[0] # CAMBIAR
        #         case _:
        #             print("Opcion invalida")
        #             # Volver a menu principal
            
        #     if(instancia.VerificarExamen()):
        #         print("Obtuvo el registro")
        #     else:
        #         print("No obtuvo el registro")
        case "4": # Salir
            break
        case _:
            print("Opcion invalida")
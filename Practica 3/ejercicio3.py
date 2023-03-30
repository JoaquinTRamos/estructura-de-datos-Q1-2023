import random as rdm
import datetime as dt

class Persona:
    def __init__(self, dia_nac: int, mes_nac: int, anno_nac: int, nombre: str = "", sexo: str = "H") -> None:
        self.nombre = nombre
        self.fecha_nac = dt.datetime(anno_nac,mes_nac,dia_nac)
        self.dni = rdm.randrange(10000000,99999999)
        self.sexo = sexo
        
    def esMayor(self):
        edad = dt.datetime.now() - self.fecha_nac
        return edad.days >= (18 * 365)
    
    def pedirInfo(self):
        return [self.nombre, self.dni, int((dt.datetime.now() - self.fecha_nac).days/(365)), self.sexo]

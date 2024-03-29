class Camion():
    def __init__(self,patente,carga,marca,anno):
        self.patente = patente
        self.carga = carga
        self.marca = marca
        self.anno = anno
        pass

    def __eq__(self, otro):
        return self.carga == otro.carga and self.anno == otro.anno and self and self.patente == otro.patente

    def __str__(self):
        return("El camion de patente {}, marca {} y anno {}, carga {} toneladas mensuales".format(self.patente, self.marca, self.anno, self.carga))
    

furgon1 = Camion("HP 321",450,"Ford",2000)
furgon2 = Camion("HP 221",700,"IVECO",2013)

print(furgon1==furgon2)
print(furgon1 is furgon2)

furgon1 = Camion("HP 321",450,"Ford",2000)
furgon2 = Camion("HP 321",450,"IVECO",2000)

print(furgon1==furgon2)
print(furgon1 is furgon2)

furgon1 = Camion("HP 321",450,"IVECO",2000)
furgon2 = Camion("HP 321",450,"IVECO",2000)

print(furgon1==furgon2)
print(furgon1 is furgon2)
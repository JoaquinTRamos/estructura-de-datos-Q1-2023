class Date:
    def __init__(self, dia:int = 1, mes:int = 1, anno:int = 1900) -> None:
        self.dia = dia if 0 < len(str(dia)) <= 2 else 1
        self.mes = mes if 0 < len(str(mes)) <= 2 else 1
        self.anno = anno if len(str(anno)) == 4 else 1900
        pass

    def formatoStandard(self) -> str:
        return f"{self.anno}-{self.mes}-{self.dia}"
    
    def formatoUniversal(self) -> str:
        return f"{self.mes}-{self.dia}-{self.anno}"




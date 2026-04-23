class Horario:
    def __init__(self, dias: str, hora_apertura: str, hora_cierre: str):
        self.__dias = dias
        self.__hora_apertura = hora_apertura
        self.__hora_cierre = hora_cierre

    def mostrar_horario(self):
        print(f"Horario: {self.__dias} de {self.__hora_apertura} a {self.__hora_cierre}")

    def __str__(self):
        return f"{self.__dias} {self.__hora_apertura}-{self.__hora_cierre}"
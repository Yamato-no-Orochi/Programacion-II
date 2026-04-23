class Estudiante:
    def __init__(self, codigo: str, nombre: str):
        self.__codigo = codigo
        self.__nombre = nombre

    def mostrar_info(self):
        print(f"Estudiante: {self.__nombre} (Código: {self.__codigo})")

    def get_nombre(self):
        return self.__nombre

    def __str__(self):
        return f"{self.__nombre} ({self.__codigo})"
class Autor:
    def __init__(self, nombre: str, nacionalidad: str):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Autor: {self.__nombre}, Nacionalidad: {self.__nacionalidad}")

    def __str__(self):
        return f"{self.__nombre} ({self.__nacionalidad})"
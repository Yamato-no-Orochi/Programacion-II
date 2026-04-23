class Pagina:
    def __init__(self, numero: int, contenido: str):
        self.__numero = numero
        self.__contenido = contenido

    def get_numero(self):
        return self.__numero

    def __str__(self):
        return f"Página {self.__numero}: {self.__contenido[:30]}..."
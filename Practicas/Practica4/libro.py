from pagina import Pagina

class Libro:
    def __init__(self, titulo: str, isbn: str, num_paginas: int):
        self.__titulo = titulo
        self.__isbn = isbn
        
        self.__paginas = []
        for i in range(1, num_paginas + 1):
            contenido = f"Contenido de la página {i} del libro {titulo}"
            self.__paginas.append(Pagina(i, contenido))

    def get_titulo(self):
        return self.__titulo

    def get_isbn(self):
        return self.__isbn

    def leer(self):
        print(f"\n Leyendo '{self.__titulo}' ")
        for pag in self.__paginas:
            print(pag)

    def __str__(self):
        return f"Libro: {self.__titulo} (ISBN: {self.__isbn})"
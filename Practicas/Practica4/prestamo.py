from datetime import datetime

class Prestamo:
    def __init__(self, estudiante, libro):
        self.__estudiante = estudiante      
        self.__libro = libro                
        self.__fecha_prestamo = datetime.now()
        self.__fecha_devolucion = None

    def devolver(self):
        self.__fecha_devolucion = datetime.now()

    def mostrar_info(self):
        print(f"Préstamo:\n  Estudiante: {self.__estudiante.get_nombre()}\n  Libro: {self.__libro.get_titulo()}\n  Fecha préstamo: {self.__fecha_prestamo}")
        if self.__fecha_devolucion:
            print(f"  Fecha devolución: {self.__fecha_devolucion}")
        else:
            print("  Estado: No devuelto aún")

    def __str__(self):
        return f"Préstamo de {self.__libro.get_titulo()} a {self.__estudiante.get_nombre()}"
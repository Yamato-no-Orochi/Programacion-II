from horario import Horario
from prestamo import Prestamo

class Biblioteca:
    def __init__(self, nombre: str, dias: str, apertura: str, cierre: str):
        self.__nombre = nombre
        
        self.__horario = Horario(dias, apertura, cierre)
        self.__libros = []          
        self.__autores = []         
        self.__prestamos_activos = []  

    def agregar_libro(self, libro):
        if libro not in self.__libros:
            self.__libros.append(libro)
            print(f" Libro '{libro.get_titulo()}' agregado a la biblioteca.")
        else:
            print(f"El libro '{libro.get_titulo()}' ya existe.")

    def agregar_autor(self, autor):
        if autor not in self.__autores:
            self.__autores.append(autor)
            print(f" Autor '{autor}' registrado en la biblioteca.")
        else:
            print(f"El autor '{autor}' ya está registrado.")

    def prestar_libro(self, estudiante, libro):
        if libro not in self.__libros:
            print(f"El libro '{libro.get_titulo()}' no está disponible en la biblioteca.")
            return

        prestamo = Prestamo(estudiante, libro)
        self.__prestamos_activos.append(prestamo)
        
        self.__libros.remove(libro)
        print(f" Préstamo realizado: {estudiante.get_nombre()} -> {libro.get_titulo()}")

    def mostrar_estado(self):
        print("\n" + "="*50)
        print(f" BIBLIOTECA: {self.__nombre}")
        self.__horario.mostrar_horario()
        print("\n Libros disponibles ")
        if self.__libros:
            for l in self.__libros:
                print(f"  • {l}")
        else:
            print("  No hay libros disponibles.")
        print("\n Autores registrados ")
        if self.__autores:
            for a in self.__autores:
                print(f"  • {a}")
        else:
            print("  No hay autores registrados.")
        print("\n Préstamos activos ")
        if self.__prestamos_activos:
            for p in self.__prestamos_activos:
                print(f"  • {p}")
        else:
            print("  No hay préstamos activos.")
        print("="*50)

    def cerrar_biblioteca(self):
        print(f"\n Cerrando biblioteca {self.__nombre}...")
        
        self.__prestamos_activos.clear()
        print("Todos los préstamos han sido cancelados.")
from biblioteca import Biblioteca
from libro import Libro
from autor import Autor
from estudiante import Estudiante

def main():
    bib = Biblioteca("Biblioteca Central UMSA", "Lun-Vie", "08:00", "20:00")

    libro1 = Libro("Cien años de soledad", "978-84-376-0494-7", 3)
    libro2 = Libro("El principito", "978-84-376-0495-4", 2)
    libro3 = Libro("Python para todos", "978-84-376-0496-1", 4)

    autor1 = Autor("Gabriel García Márquez", "Colombiana")
    autor2 = Autor("Antoine de Saint-Exupéry", "Francesa")
    autor3 = Autor("Raúl González", "Boliviana")

    bib.agregar_libro(libro1)
    bib.agregar_libro(libro2)
    bib.agregar_libro(libro3)
    bib.agregar_autor(autor1)
    bib.agregar_autor(autor2)
    bib.agregar_autor(autor3)

    est1 = Estudiante("20210001", "Ana Maria Perez")
    est2 = Estudiante("20210002", "Luis Fernandez")

    bib.mostrar_estado()

    bib.prestar_libro(est1, libro1)
    bib.prestar_libro(est2, libro2)

    bib.mostrar_estado()

    bib.prestar_libro(est1, libro1)  
    bib.cerrar_biblioteca()
    bib.mostrar_estado()

    print("\n Los libros siguen existiendo fuera de la biblioteca ")
    libro1.leer()
    print("\n Los autores también ")
    autor1.mostrar_info()

if __name__ == "__main__":
    main()
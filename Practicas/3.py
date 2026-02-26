import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("El coeficiente 'a' no puede ser 0 (no es ecuación cuadrática)")
        self.__a = a  
        self.__b = b
        self.__c = c
        self.__discriminante = self.__calcular_discriminante()
        print(f"✓ Ecuación cuadrática creada: {a}x² + {b}x + {c} = 0")
    def __del__(self):
        print(f"✗ Ecuación cuadrática destruida")
    def __calcular_discriminante(self):
        return self.__b**2 - 4 * self.__a * self.__c
    def getDiscriminante(self):
        return self.__discriminante
    def getRaiz1(self):
        if self.__discriminante >= 0:
            return (-self.__b + math.sqrt(self.__discriminante)) / (2 * self.__a)
        return 0
    def getRaiz2(self):
        if self.__discriminante >= 0:
            return (-self.__b - math.sqrt(self.__discriminante)) / (2 * self.__a)
        return 0
    def getTipoSolucion(self):
        if self.__discriminante > 0:
            return "dos raíces reales"
        elif self.__discriminante == 0:
            return "una raíz real (doble)"
        else:
            return "raíces complejas"
    def __str__(self):
        signo_b = "+" if self.__b >= 0 else "-"
        signo_c = "+" if self.__c >= 0 else "-"
        return f"{self.__a}x² {signo_b} {abs(self.__b)}x {signo_c} {abs(self.__c)} = 0"

def test_ecuacion_cuadratica_poo():
    valores = input("Ingrese a, b, c: ").split()
    a, b, c = map(float, valores)   
    try:
        ecuacion = EcuacionCuadratica(a, b, c)   
        print(f"\nEcuación: {ecuacion}")
        discriminante = ecuacion.getDiscriminante()
        print(f"Discriminante: {discriminante:.4f}")
        print(f"Tipo de solución: {ecuacion.getTipoSolucion()}")
        if discriminante > 0:
            r1 = ecuacion.getRaiz1()
            r2 = ecuacion.getRaiz2()
            print(f"La ecuación tiene dos raíces: {r1:.6f} y {r2:.6f}")
        elif discriminante == 0:
            r = ecuacion.getRaiz1()
            print(f"La ecuación tiene una raíz: {r}")
        else:
            print("La ecuación no tiene raíces reales")         
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    test_ecuacion_cuadratica_poo()
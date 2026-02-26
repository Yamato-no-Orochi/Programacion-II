import math
class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a  
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        print("✓ Sistema de ecuaciones creado")
    
    def __del__(self):
        print("✗ Sistema de ecuaciones destruido")
    def getA(self): return self.__a
    def getB(self): return self.__b
    def getC(self): return self.__c
    def getD(self): return self.__d
    def getE(self): return self.__e
    def getF(self): return self.__f
    
    def tieneSolucion(self):
        determinante = self.__a * self.__d - self.__b * self.__c
        return abs(determinante) > 1e-10  
    def getX(self):
        if self.tieneSolucion():
            denominador = self.__a * self.__d - self.__b * self.__c
            return (self.__e * self.__d - self.__b * self.__f) / denominador
        return None  
    def getY(self):
        if self.tieneSolucion():
            denominador = self.__a * self.__d - self.__b * self.__c
            return (self.__a * self.__f - self.__e * self.__c) / denominador
        return None
    def __str__(self):
        return (f"Sistema: {self.__a}x + {self.__b}y = {self.__e}\n"
                f"         {self.__c}x + {self.__d}y = {self.__f}")

def test_ecuacion_lineal_poo():
    valores = input("Ingrese a, b, c, d, e, f: ").split()
    a, b, c, d, e, f = map(float, valores)
    
    ecuacion = EcuacionLineal(a, b, c, d, e, f)
    
    print(f"\n{ecuacion}")
    
    if ecuacion.tieneSolucion():
        x = ecuacion.getX()
        y = ecuacion.getY()
        print(f"\n Solución: x = {x}, y = {y}")
    else:
        print("\n La ecuación no tiene solución")
    print(f"\nCoeficientes: a={ecuacion.getA()}, b={ecuacion.getB()}, "
          f"c={ecuacion.getC()}, d={ecuacion.getD()}, e={ecuacion.getE()}, f={ecuacion.getF()}")

if __name__ == "__main__":
    test_ecuacion_lineal_poo()
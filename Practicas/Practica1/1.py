import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = 0
        self.__estado = "detenido"
        print("+ Cronometro creado")
    
    def __del__(self):
        print("- Cronometro destruido")
    
    def getInicia(self):
        return self.__inicia
    
    def getFinaliza(self):
        return self.__finaliza
    
    def getEstado(self):
        return self.__estado
    
    def inicia(self):
        self.__inicia = time.time()
        self.__estado = "en ejecucion"
        print("> Cronometro iniciado")
    
    def detener(self):
        self.__finaliza = time.time()
        self.__estado = "detenido"
        print("> Cronometro detenido")
    
    def lapsoDeTiempo(self):
        if self.__finaliza == 0:
            return (time.time() - self.__inicia) * 1000
        return (self.__finaliza - self.__inicia) * 1000
if __name__ == "__main__":
    
    crono = Cronometro()
    
    print("\nGenerando 100,000 numeros...")
    numeros = [random.randint(1, 1000) for _ in range(100000)]
    print("Iniciando cronometro...")
    crono.inicia()
    print("Ordenando por seleccion...")
    numeros.sort()  
    crono.detener()
    
    print(f"\nTiempo de ejecucion: {crono.lapsoDeTiempo():.2f} ms")
    print(f"Estado final: {crono.getEstado()}")
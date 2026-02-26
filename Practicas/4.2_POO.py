import math

class Estadistica:
    def __init__(self):
        self.__datos = []      
        self.__cantidad = 0   
        print("✓ Objeto Estadística creado")
    def __del__(self):
        print("✗ Objeto Estadística destruido")
    def agregar_dato(self, valor):
        self.__datos.append(float(valor))
        self.__cantidad = len(self.__datos)  
    def agregar_datos_lista(self, lista):
        for valor in lista:
            self.__datos.append(float(valor))
        self.__cantidad = len(self.__datos) 
    def limpiar_datos(self):
        self.__datos = []
        self.__cantidad = 0
        print("✓ Datos eliminados")
    def get_datos(self):
        return self.__datos.copy()
    def get_cantidad(self):
        return self.__cantidad
    def promedio(self):
        if self.__cantidad == 0:
            return 0
        suma = 0
        for i in range(self.__cantidad):
            suma += self.__datos[i]
        return suma / self.__cantidad
    def desviacion(self):
        if self.__cantidad < 2:
            return 0
        prom = self.promedio()
        suma_cuadrados = 0
        for i in range(self.__cantidad):
            suma_cuadrados += (self.__datos[i] - prom) ** 2
        return math.sqrt(suma_cuadrados / (self.__cantidad - 1))
    def mostrar_estadisticas(self):
        print(f"Promedio: {self.promedio()}")
        print(f"Desviación estándar: {self.desviacion():.5f}")
    def __str__(self):
        if self.__cantidad == 0:
            return "Estadística (sin datos)"
        return f"Estadística[{self.__cantidad} datos]: min={min(self.__datos)}, max={max(self.__datos)}"
    
def main_poo():
    estadistica = Estadistica()
    print("\nIngrese 10 números separados por espacio:")
    entrada = input("→ ")
    numeros = []
    for valor in entrada.split():
        numeros.append(float(valor))
    if len(numeros) != 10:
        print(f"Error: Se esperaban 10 números, pero ingresó {len(numeros)}")
        return
    estadistica.agregar_datos_lista(numeros)
    print(f"\n{estadistica}")
    
    estadistica.mostrar_estadisticas()   
if __name__ == "__main__":
    main_poo()
import math

def promedio(datos):
    suma_total = 0
    cantidad = len(datos) 
    for i in range(cantidad):
        suma_total += datos[i]
    
    return suma_total / cantidad
def desviacion(datos, prom):

    cantidad = len(datos)
    suma_cuadrados = 0
    for i in range(cantidad):
        suma_cuadrados += (datos[i] - prom) ** 2
    
    return math.sqrt(suma_cuadrados / (cantidad - 1))
def main_modular():
    print("\nIngrese 10 números separados por espacio:")
    entrada = input("→ ")
    
    numeros = []
    for valor in entrada.split():
        numeros.append(float(valor))
    
    if len(numeros) != 10:
        print(f"Error: Se esperaban 10 números, pero ingresó {len(numeros)}")
        return   
    prom = promedio(numeros)
    desv = desviacion(numeros, prom)
    print(f"El promedio es {prom}")
    print(f"La desviación estandard es {desv:.5f}")
if __name__ == "__main__":
    main_modular()
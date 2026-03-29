import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidasInicial = numeroDeVidas   
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = self.numeroDeVidasInicial
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0   
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)   
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)   
        print("Adivina un número entre 0 y 10.")
        while True:
            try:
                intento = int(input("Ingresa tu número: "))
            except ValueError:
                print("Por favor ingresa un número entero.")
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if not self.quitaVida():
                    print("¡Te quedaste sin vidas!")
                    break
                else:
                    if intento < self.numeroAAdivinar:
                        print("El número a adivinar es MAYOR.")
                    else:
                        print("El número a adivinar es MENOR.")
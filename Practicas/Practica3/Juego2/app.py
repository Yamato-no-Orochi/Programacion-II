from juegos import JuegoAdivinaNumero, JuegoAdivinaPar, JuegoAdivinaImpar

def main():
    print("Juego Adivina Número")
    juego1 = JuegoAdivinaNumero(3)
    juego1.juega()

    print("\nJuego Adivina Número PAR")
    juego2 = JuegoAdivinaPar(3)
    juego2.juega()

    print("\n Juego Adivina Número IMPAR")
    juego3 = JuegoAdivinaImpar(3)
    juego3.juega()

if __name__ == "__main__":
    main()
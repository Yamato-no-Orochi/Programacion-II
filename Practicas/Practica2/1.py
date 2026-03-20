import math
class MiPunto:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def distancia(self, *args):
        if len(args) == 1 and isinstance(args[0], MiPunto):
            otro = args[0]
            dx = self.__x - otro.getX()
            dy = self.__y - otro.getY()
            return math.hypot(dx, dy)
        elif len(args) == 2:
            x, y = args
            dx = self.__x - x
            dy = self.__y - y
            return math.hypot(dx, dy)
        else:
            raise TypeError("distancia() espera 1 (MiPunto) o 2 (float, float) argumentos")
if __name__ == "__main__":
    p1 = MiPunto()
    p2 = MiPunto(10, 30.5)
    print(f"p1 = ({p1.getX()}, {p1.getY()})")
    print(f"p2 = ({p2.getX()}, {p2.getY()})")
    print(f"Distancia de p1 a p2: {p1.distancia(p2):.2f}")
    print(f"Distancia de p2 al origen: {p2.distancia(0, 0):.2f}")
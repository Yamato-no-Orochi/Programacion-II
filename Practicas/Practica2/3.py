import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __add__(self, otro):
        return Vector3D(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    def __sub__(self, otro):
        return Vector3D(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    def __mul__(self, otro):
        if isinstance(otro, (int, float)):
            return Vector3D(self.x * otro, self.y * otro, self.z * otro)
        raise TypeError("Solo se puede multiplicar por un escalar")
    def __rmul__(self, otro):
        return self.__mul__(otro)
    def __matmul__(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    def cross(self, otro):
        cx = self.y * otro.z - self.z * otro.y
        cy = self.z * otro.x - self.x * otro.z
        cz = self.x * otro.y - self.y * otro.x
        return Vector3D(cx, cy, cz)
    def longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normalizar(self):
        mag = self.longitud()
        if mag == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x/mag, self.y/mag, self.z/mag)
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"
if __name__ == "__main__":
    a = Vector3D(1, 0, 0)
    b = Vector3D(0, 1, 0)
    print("a =", a)
    print("b =", b)
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("3 * a =", 3 * a)
    print("a @ b =", a @ b)
    print("a × b =", a.cross(b))
    print("|a| =", a.longitud())
    print("a normalizado =", a.normalizar())
import math

class AlgebraVectorial:
    def perpendicular(self, a, b, modo='diagonales'):
        if modo == 'diagonales':
            suma = (a[0]+b[0], a[1]+b[1], a[2]+b[2])
            resta = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
            return math.isclose(self._mod(suma), self._mod(resta))
        elif modo == 'producto_punto':
            return math.isclose(a[0]*b[0] + a[1]*b[1] + a[2]*b[2], 0.0)
        else:
            raise ValueError("Modo no soportado")
    def paralela(self, a, b, modo='escalar'):
        if modo == 'escalar':
            if all(v == 0 for v in b):
                return all(v == 0 for v in a)
            r = None
            for i in range(3):
                if b[i] != 0:
                    r_ = a[i] / b[i]
                    if r is None:
                        r = r_
                    elif not math.isclose(r, r_):
                        return False
                elif a[i] != 0:
                    return False
            return True
        elif modo == 'producto_vectorial':
            cross = (a[1]*b[2] - a[2]*b[1],
                     a[2]*b[0] - a[0]*b[2],
                     a[0]*b[1] - a[1]*b[0])
            return all(math.isclose(x, 0.0) for x in cross)
        else:
            raise ValueError("Modo no soportado")
    
    def proyeccion(self, a, b):
        dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
        mag2 = b[0]**2 + b[1]**2 + b[2]**2
        if mag2 == 0:
            return (0,0,0)
        factor = dot / mag2
        return (factor*b[0], factor*b[1], factor*b[2])
    
    def componente(self, a, b):
        dot = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
        mag = math.sqrt(b[0]**2 + b[1]**2 + b[2]**2)
        return dot / mag if mag != 0 else 0.0
    
    @staticmethod
    def _mod(v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
av = AlgebraVectorial()
a = (1, 0, 0)
b = (0, 1, 0)

print("Perpendicular (diagonales):", av.perpendicular(a, b))
print("Perpendicular (producto punto):", av.perpendicular(a, b, 'producto_punto'))
print("Paralela (escalar):", av.paralela(a, b))
print("Paralela (producto vectorial):", av.paralela(a, b, 'producto_vectorial'))
print("Proyección de a sobre b:", av.proyeccion(a, b))
print("Componente de a en b:", av.componente(a, b))
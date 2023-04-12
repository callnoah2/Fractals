import Fractal

class Burningship(Fractal):
    def __init__(self, c, z, maxIter):
        super().__init__(c, z, maxIter)

    def count(self, c, maxIter):
        z = complex(0, 0)
        for i in range(maxIter):
            z = (abs(z.real) + abs(z.imag)*1j)**2 + c
            if abs(z) > 2:
                return i
        return maxIter
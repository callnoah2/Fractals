import Fractal

class Julia(Fractal):
    def __init__(self, c, z, maxIter):
        super().__init__(c, z, maxIter)

    def count(self, z, maxIter):
        c = self.c
        for i in range(maxIter):
            z = z * z + c
            if abs(z) > 2:
                return i
        return maxIter
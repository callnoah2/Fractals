from Fractal import Fractal

class SpiderFrac(Fractal):
    def __init__(self, c, maxIter):
        super().__init__(c, maxIter)

    def count(self, c, maxIter):
        z = complex(0, 0)
        for i in range(maxIter):
            z = z * z + c
            c = (c/2) + z
            if abs(z) > 2:
                return i
        return maxIter
from Fractal import Fractal

class JuliaFrac(Fractal):
    def __init__(self, z, maxIter):
        super().__init__( z, maxIter)

    def count(self, z, maxIter):
        c = complex(0,0)
        for i in range(maxIter):
            z = z * z + c
            if abs(z) > 2:
                return i
        return maxIter
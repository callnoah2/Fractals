from Fractal import Fractal


class Mandelbrot4Frac(Fractal):
    def __init__(self, c, maxIter):
        super().__init__(c, maxIter)

    def count(self, c, maxIter):

        z = complex(0, 0)
        for i in range(maxIter):
            z = z * z * z * z + c
            if abs(z) > 2:
                return i
        return maxIter
import Fractal
class NewtonFrac(Fractal):
    def __init__(self, c, z, maxIter):
        super().__init__(c, z, maxIter)

    def count(self, c, maxIter):
        EPSILON = 0.000001
        ROOTS = [1, -0.5 + 0.5j * 3 ** 0.5, -0.5 - 0.5j * 3 ** 0.5]

        z = complex(0, 0)
        for i in range(maxIter):
            dz = 3 * z ** 2
            z = z - (z ** 3 - 1) / dz

            for root in ROOTS:
                diff = z - root
                if abs(diff.real) < EPSILON and abs(diff.imag) < EPSILON:
                    return i

        return maxIter
from Fractal import Fractal
class NewtonFrac(Fractal):
    def __init__(self, c, maxIter):
        super().__init__(c, maxIter)

    def count(self, c, maxIter):
        EPSILON = 0.000001
        ROOTS = [1, -0.5 + 0.5j * 3 ** 0.5, -0.5 - 0.5j * 3 ** 0.5]

        z = c
        for i in range(maxIter):
            dz = 3 * z ** 2
            nz = (z**3 -1)
            if dz == 0:
                dz += 1
            z = z - (nz / dz)

            for root in ROOTS:
                diff = z - root
                if abs(diff.real) < EPSILON and abs(diff.imag) < EPSILON:
                    return i

        return maxIter
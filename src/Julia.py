import Fractal


class Julia(Fractal):
    def __init__(self, c, z, maxIter):
        super().__init__(c, z, maxIter)

    def count(self):
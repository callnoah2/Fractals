class Fractal:
    def __init__(self, c, z, maxIter):
        self.c = c
        self.z = z
        self.maxIter = maxIter

    def count(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
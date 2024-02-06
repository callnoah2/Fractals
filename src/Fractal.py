class Fractal:
    def __init__(self, z, maxIter):
        self.z = z
        self.maxIter = maxIter

    def count(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
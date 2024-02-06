
class Palette:
    def __init__(self):
        pass

    def makePal(self, maxIter):
        raise NotImplementedError("Subclass needs to do this.")
    def getColor(self,value):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")
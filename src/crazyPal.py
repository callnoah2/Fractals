import Palette
from colour import Color
class crazyPal(Palette):
    def __init__(self):
        super().__init__()

    # def paletteEquation(self, palette, start, end, size):
    #     for color in start.range_to(end, size):
    #         palette.append(color.hex_l)
    #     return palette
    def makePal(self, maxIter):
        palette = []
        start = ""
        end = ""
        for color in start.range_to(end, maxIter):
            palette.append(color.hex_l)
        return palette
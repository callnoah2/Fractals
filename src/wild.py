from Palette import Palette
from colour import Color

class wildPal(Palette):
    def __init__(self):
        super().__init__()

    def paletteEquation(self, palette, start, end, maxIter):
        startColor = Color(start)
        endColor = Color(end)
        for color in startColor.range_to(endColor, maxIter):
            if color.hex_l not in palette:
                palette.append(color.hex_l)
        return palette

    def makePal(self, maxIter):
        palette = []
        start = "green"
        end = "red"
        maxIter = int(maxIter/4) + 2
        palette += self.paletteEquation(palette, start, end, maxIter)
        start = end
        end = "blue"
        palette += self.paletteEquation(palette, start, end, maxIter)
        start = end
        end = "yellow"
        palette += self.paletteEquation(palette, start, end, maxIter)
        start = end
        end = "pink"
        palette += self.paletteEquation(palette, start, end, maxIter)
        return palette

    def getColor(self, palette, count):
        return palette[count]
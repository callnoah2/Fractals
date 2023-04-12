import Palette
from wild import wildPal
from crazyPal import CrazyPal
def makePalette(paletteName, fractalInfo):
    palettes = {
        "wildPal": wildPal(),
        "crazyPal": CrazyPal()
    }

    if paletteName in palettes:
        palette = palettes[paletteName].makePal(fractalInfo.maxIterations)
        return palette
    else:
        raise NotImplementedError("Invalid palette requested")
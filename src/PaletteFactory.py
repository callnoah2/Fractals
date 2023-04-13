import Palette
from Palette import Palette
from wild import wildPal
from crazyPal import CrazyPal
def makePalette(paletteName):
    palettes = {
        "wildPal": wildPal(),
        "crazyPal": CrazyPal()
    }

    if paletteName in palettes:
        Palette = palettes[paletteName]
        return Palette
    else:
        raise NotImplementedError("Invalid palette requested")
import Palette
from Palette import Palette
from wild import wildPal
from crazyPal import CrazyPal
from awesome import awesomePal
def makePalette(paletteName):
    palettes = {
        "wildPal": wildPal(),
        "crazyPal": CrazyPal(),
        "awesome": awesomePal()
    }

    if paletteName in palettes:
        Palette = palettes[paletteName]
        return Palette
    else:
        raise NotImplementedError("Invalid palette requested")
import Palette
from Palette import Palette
from wild import wildPal
from crazyPal import CrazyPal
from awesome import awesomePal
from simple import simplePal
from slow import slowPal
def makePalette(paletteName):
    palettes = {
        "wild": wildPal(),
        "crazy": CrazyPal(),
        "awesome": awesomePal(),
        "simple": simplePal(),
        "slow": slowPal()
    }

    if paletteName in palettes:
        Palette = palettes[paletteName]
        return Palette
    else:
        raise NotImplementedError("Invalid palette requested")
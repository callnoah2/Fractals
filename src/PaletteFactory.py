import wild, crazyPal, Palette
def makePalette(paletteName, fractalInfo):
    palettes = {
        "wild": wild,
        "crazyPal": crazyPal
    }

    if paletteName in palettes:
        return palettes[paletteName]()
    else:
        raise NotImplementedError("Invalid palette requested")
#!/usr/bin/env python3  	  	  


import sys
import FractalParser
import FractalFactory
import ImagePainter

file = "default"
paletteName = "crazy"
if len(sys.argv) == 3:
    file = sys.argv[1]
    paletteName = sys.argv[2]
elif len(sys.argv) == 2:
    file = sys.argv[1]

FractalInfo = FractalParser.parse(file)
fractal = FractalFactory.makeFractal(FractalInfo)
ImagePainter.make_picture_of_fractal(FractalInfo, fractal, paletteName, file)



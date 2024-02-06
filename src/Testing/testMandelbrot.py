#!/usr/bin/env python3  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  


import unittest  	  	  
from Mandelbrot import mBrotIter
import Palette
from ImagePainter import pixSoFar


# autocmd BufWritePost <buffer> !python3 runTests.py  	  	  

class TestMandelbrot(unittest.TestCase):


    def test_pixelColorOrIndex(self):  	  	  
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""  	  	  
        # test the pixel color...
        maxIter = 115
        self.assertEqual(Palette.getColor(mBrotIter(complex(0, 0), maxIter), 1), '#7D387D')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.751, 1.1075), maxIter), 1), '#E0DC9C')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.2, 1.1075), maxIter), 1), '#CDDC93')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.75, 0.1075), maxIter), 1), '#79D078')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.748, 0.1075), maxIter), 1), '#59C0BD')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.7562500000000001, 0.078125), maxIter), 1), '#6ECB8A')


    def test_pixelsWrittenSoFar(self):
        canvasSize = 640
        """Progress bar produces correct output"""  	  	  
        self.assertEqual(pixSoFar(canvasSize, 0), 100)
        self.assertEqual(round(pixSoFar(canvasSize, 7)), 99)
        self.assertEqual(round(pixSoFar(canvasSize, 321)), 50)
        self.assertEqual(round(pixSoFar(canvasSize, 130)), 80)
        self.assertEqual(round(pixSoFar(canvasSize, 170)), 73)
        self.assertEqual(pixSoFar(canvasSize, 640), 0)

    def test_palleteLength(self):  	  	  
        """Palette contains the expected number of colors"""  	  	  
        self.assertEqual(Palette.getLen(1), 111)

    def test_lastColorisRight(self):
        indx = len(Palette.p) - 1
        self.assertEqual(Palette.p[indx], '#7D387D')

if __name__ == '__main__':  	  	  
    unittest.main()  	  	  

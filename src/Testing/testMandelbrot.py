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
        self.assertEqual(Palette.getColor(mBrotIter(complex(0, 0)), maxIter), '#7D387D')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.751, 1.1075)), maxIter), '#E0DC9C')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.2, 1.1075)), maxIter), '#CDDC93')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.75, 0.1075)), maxIter), '#79D078')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.748, 0.1075)), maxIter), '#59C0BD')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.7562500000000001, 0.078125)), maxIter), '#6ECB8A')


    def test_pixelsWrittenSoFar(self):  	  	  
        """Progress bar produces correct output"""  	  	  
        self.assertEqual(pixSoFar(1, 600), '[100% =================================]')
        self.assertEqual(pixSoFar(7, 7), '[ 99% =================================]')
        self.assertEqual(pixSoFar(257, 321), '[ 50% ================                 ]')
        self.assertEqual(pixSoFar(256, 256), '[ 50% =================                ]')
        self.assertEqual(pixSoFar(100, 100), '[ 80% ===========================      ]')
        self.assertEqual(pixSoFar(640, 480), '[-25%                                  ]')
        self.assertEqual(pixSoFar(137, 1000), '[ 73% ========================         ]')
        self.assertEqual(pixSoFar(512, 0), '[  0%                                  ]')

    def test_palleteLength(self):  	  	  
        """Palette contains the expected number of colors"""  	  	  
        self.assertEqual(Palette.getLen(), 100)


if __name__ == '__main__':  	  	  
    unittest.main()  	  	  

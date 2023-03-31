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


import sys
from FractalInformation import fractalDict
import ImagePainter


canvasSize = 512

if len(sys.argv) < 2:
    print("Please provide the name of the fractal as an argument.")
    for i in fractalDict:
        print("\t", i)
    sys.exit(1)
else:
    fractal = sys.argv[1]

fractalList = list(fractalDict.keys())

if fractal in fractalDict:
    fractalParam = fractalDict[fractal]
    if fractal in fractalList[:7]:
        whichFractal = 1
    else:
        whichFractal = 2
    ImagePainter.make_picture_of_fractal(fractalParam, canvasSize, whichFractal, fractal)
else:
    print(f"ERROR: {fractal} is not a valid fractal")
    print("Please choose one of the following:")
    for f in fractalDict:
        print(f"\t{f}")
    sys.exit(1)


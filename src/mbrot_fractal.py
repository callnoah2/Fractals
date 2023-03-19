#!/usr/bin/env python3  	  	  
# Mandelbrot Set Visualizer  	  	  

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
import time  	  	  
from tkinter import Tk, Canvas, PhotoImage, mainloop  	  	  
from math import sqrt, cos, cosh, sin, sinh, remainder, acos, acosh, asin, asinh  	  	  

# These are the imports that I usually import  	  	  
import turtle  	  	  
import os  	  	  
import os.path  	  	  
import sys  	  	  
import time  	  	  
import math  	  	  

# this import caused problems on my Windows computer...  	  	  
# import numpy  	  	  

GRAPEFRUIT_PINK = '#E8283F'  	  	  
LEMON = '#FDFF00'  	  	  
LIME_GREEN = '#89FF00'  	  	  
KUMQUAT = '#FAC309'  	  	  
MAX_ITERATIONS = -1  	  	  
POMELLO = '#2FFF00'  	  	  
TANGERINE = '#F7B604'  	  	  
WHITE = '#FFFFFF'  	  	  
CUSTARD = '#E1D89F'  	  	  
PISTACHIO = '#A8D786'  	  	  
MINT = '#6ECB8A'  	  	  
ELDERBERRY = '#4771B2'  	  	  
CONCORD_GRAPE = '#51419C'  	  	  
PLUM = '#7D387D'  	  	  
BLACK = '#000000'  	  	  
# XXX: for some reason this line of code crashes the program...  	  	  
# window = Tk()  	  	  
WHITE = '#ffffff'  	  	  
#palette = [LIME_GREEN, '#a8f71b', '#c0ef34', '#d2ea4c', '#dfe563', '#e2db78',  	  	  
#        '#e0d28d', '#dfce9f', '#e0ceb1', '#e2d2c1', '#e5d9d0', '#eae1de',  	  	  
#        '#efebea', '#f7f5f5', WHITE, '#f7f5f5', '#efebea', '#eae0de',  	  	  
#        '#e5d6d0', '#e2cdc1', '#e0c5b1', '#dfbf9f', '#e0bc8d', '#e2bd78',  	  	  
#        '#e5c163', '#eac94c', '#efd634', '#f7e81b', LEMON, '#f7e81b',  	  	  
#        '#efd634', '#eac94c', '#e5c163', '#e2bd78', '#e0bc8d', '#dfbf9f',  	  	  
#        '#e0c5b1', '#e2cdc1', '#e5d6d0', '#eae0de', '#efebea', '#f7f5f5',  	  	  
#        WHITE, '#f6f5f5', '#efeaea', '#e9dfdd', '#e4d4d0', '#e1c9c1',  	  	  
#        '#dfbfb0', '#deb69f', '#deae8c', '#e0a978', '#e2a563', '#e7a54c',  	  	  
#        '#eca834', '#f3ae1b', TANGERINE, '#f3ae1b', '#eca834', '#e7a54c',  	  	  
#        '#e2a563', '#e0a978', '#deae8c', '#deb69f', '#dfbfb0', '#e1c9c1',  	  	  
#        '#e4d4d0', '#e9dfdd', '#efeaea', '#f6f5f5', WHITE, '#f6f6f5',  	  	  
#        '#efefea', '#e5e9de', '#d5e3d1', '#c3dfca', '#b4ddd1', '#a3d2db',  	  	  
#        '#91adda', '#857fdb', '#a66bdc', '#dc56df', '#e33f9d', WHITE,  	  	  
#        '#f6f5f4', '#eeeee8', '#e2e7db', '#cedead', '#beefcc', '#abdbd9',  	  	  
#        '#99beda', '#858cda', '#9c70dc', '#d159de', '#e341a4',  	  	  
#        GRAPEFRUIT_PINK, ]  	  	  

# This color palette contains 100 color steps.  	  	  
palette = [CUSTARD, '#E0DA9E', '#E0DC9C', '#DFDE9B', '#DEDF9A', '#DBDE98',  	  	  
           '#D8DE97', '#D4DD96', '#D1DD94', '#CDDC93', '#CADC92', '#C6DB91',  	  	  
           '#C3DB8F', '#BFDA8E', '#BCD98D', '#B8D98B', '#B4D88A', '#B0D889',  	  	  
           '#ACD788', PISTACHIO, '#A4D685', '#A0D684', '#9CD582', '#98D481',  	  	  
           '#94D480', '#8FD37F', '#8BD37D', '#87D27C', '#82D17B', '#7ED17A',  	  	  
           '#79D078', '#77D07A', '#76CF7C', '#75CF7E', '#73CE80', '#72CD83',  	  	  
           '#71CD85', '#70CC87', MINT, '#6DCB8C', '#6CCA8F', '#6BCA91',  	  	  
           '#69C994', '#68C896', '#67C899', '#66C79C', '#65C79F', '#63C6A2',  	  	  
           '#62C5A4', '#61C5A7', '#60C4AA', '#5FC3AD', '#5DC3B0', '#5CC2B3',  	  	  
           '#5BC1B7', '#5AC1BA', '#59C0BD', '#57BFBF', '#56BABF', '#55B5BE',  	  	  
           '#54B1BD', '#53ACBD', '#51A7BC', '#50A3BB', '#4F9EBB', '#4E99BA',  	  	  
           '#4D94B9', '#4C8FB9', '#4A8AB8', '#4985B7', '#4880B7', '#487BB5',  	  	  
           '#4876B4', ELDERBERRY, '#476CB1', '#4668AF', '#4663AE', '#465EAC',  	  	  
           '#455AAB', '#4556A9', '#4551A8', '#444DA6', '#4449A5', '#4345A3',  	  	  
           '#4543A2', '#4843A1', '#4B429F', '#4E429E', CONCORD_GRAPE,  	  	  
           '#54419B', '#574199', '#594098', '#5C4096', '#5E3F95', '#613F94',  	  	  
           '#633F92', '#653E91', '#673E8F', '#6A3D8E', '#6C3D8C', '#6D3C8B',  	  	  
           '#6F3C8A', '#713C88', '#733B87', '#753B85', '#763A84', '#783A83',  	  	  
           '#793981', '#7A3980', '#7C387E', PLUM]  	  	  

MAX_ITERATIONS = 115  	  	  
z = 0  	  	  
seven = 7.0  	  	  
TWO = 2  	  	  

img = None  	  	  

mainWindowObject = None  	  	  

# def PixelColorOrIndex(c, palette):  	  	  
#     """Return the color of the current pixel within the Mandelbrot set"""  	  	  
#     global z  	  	  
#     z = complex(0, 0)  # z0  	  	  
#  	  	  
#     global MAX_ITERATIONS  	  	  
#     global iter  	  	  
#  	  	  
#     len = MAX_ITERATIONS  	  	  
#     for iter in range(len):  	  	  
#         z = z * z + c  # Get z1, z2, ...  	  	  
#         global TWO  	  	  
#         if abs(z) > TWO:  	  	  
#             z = float(TWO)  	  	  
#             if iter >= len(palette):  	  	  
#                 iter = len(palette) - 1  	  	  
#             return palette[iter]  	  	  
#         elif abs(z) < TWO:  	  	  
#             continue  	  	  
#         elif abs(z) > seven:  	  	  
#             print("You should never see this message in production", file=sys.stderr)  	  	  
#             continue  	  	  
#             break  	  	  
#         elif abs(z) < 0:  	  	  
#             print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	  	  
#             sys.exit(1)  	  	  
#         else:  	  	  
#             pass  	  	  
#  	  	  
#     return palette[iter]  # The sequence is unbounded  	  	  

def PixelColorOrIndex(c, palette):  	  	  
    """  	  	  
    Return the color of the current pixel within the Mandelbrot set  	  	  
    - OR -  	  	  
    Return the INDEX of the color of the pixel within the Mandelbrot set  	  	  
    The INDEX corresponds to the iteration count of the for loop.  	  	  
    """  	  	  
    global z  	  	  
    z = complex(0, 0)  # z0  	  	  

    global MAX_ITERATIONS  	  	  
    global iter  	  	  

    ## if a color scheme palette is passed in, return a color from the palette  	  	  
    if palette is not None:  	  	  
        # maybe it had something to do with 'len' being an integer variable  	  	  
        # instead of a function variable.  	  	  
        # Somebody from StackOverflow suggested I do it this way  	  	  
        # IDK why, but it stopped crashing, and taht's all that matters!  	  	  
        import builtins  	  	  
        len = builtins.len  	  	  
        len = len(palette)  	  	  
        global TWO  	  	  
        for iter in range(len):  	  	  
            z = z * z + c  # Get z1, z2, ...  	  	  
            if abs(z) > TWO:  	  	  
                z = float(TWO)  	  	  
                import builtins  	  	  
                len = builtins.len  	  	  
                if iter >= len(palette):  	  	  
                    iter = len(palette) - 1  	  	  
                return palette[iter]  	  	  
            elif abs(z) < TWO:  	  	  
                continue  	  	  
            elif abs(z) > seven:  	  	  
                print("You should never see this message in production", file=sys.stderr)  	  	  
                continue  	  	  
                break  	  	  
            elif abs(z) < 0:  	  	  
                print(f"This REALLY should not have happened! z={z} iter={iter} MAX_ITERATIONS={MAX_ITERATIONS}", file=sys.stderr)  	  	  
                sys.exit(1)  	  	  
            else:  	  	  
                pass  	  	  

    ## if a color scheme palette is NOT passed in, return the number of the color  	  	  
    elif palette is None:  	  	  
        len = MAX_ITERATIONS  	  	  
        for iter in range(len):  	  	  
            z = z * z + c  # Get z1, z2, ...  	  	  
            TWO = float(2)  	  	  
            if abs(z) > TWO:  	  	  
                z = float(TWO)  	  	  
                if iter == MAX_ITERATIONS:  	  	  
                    iter = MAX_ITERATIONS - 1  	  	  
                return iter  	  	  
            elif abs(z) <= TWO:  	  	  
                continue  	  	  

    # Code borrowed from StackOverflow  	  	  
    #  	  	  
    # XXX: the program used to crash with the error  	  	  
    #   TypeError: 'int' object is not callable  	  	  
    #  	  	  
    # Maybe it had something to do with 'len' being an integer variable  	  	  
    # instead of a function variable.  	  	  
    # Somebody from StackOverflow suggested I do it this way  	  	  
    # IDK why, but it stopped crashing, and taht's all that matters!  	  	  
    import builtins  	  	  
    len = builtins.len  	  	  
    if palette is None:  	  	  
        return iter  	  	  
    elif iter >= len(palette):  	  	  
        iter = len(palette) - 1  	  	  
    return palette[iter]  # The sequence is unbounded  	  	  



def paint(fractals, imagename, window):  	  	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    This code creates an image which is 640x640 pixels in size."""  	  	  

    global palette  	  	  
    global img  	  	  

    fractal = fractals[imagename]  	  	  

    # Figure out how the boundaries of the PhotoImage relate to coordinates on  	  	  
    # the imaginary plane.  	  	  
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)  	  	  
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)  	  	  
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)  	  	  
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)  	  	  

    # Display the image on the screen  	  	  
    canvas = Canvas(window, width=512, height=512, bg='#000000')  	  	  
    canvas.pack()  	  	  
    canvas.create_image((256, 256), image=img, state="normal")  	  	  

    # At this scale, how much length and height on the imaginary plane does one  	  	  
    # pixel take?  	  	  
    pixelsize = abs(maxx - minx) / 512  	  	  

    portion = 0  	  	  
    total_pixels = 512 * 512  # 262144  	  	  
    # loop  	  	  
    for row in range(512, 0, -1):  	  	  
        cc = []  	  	  
        for col in range(512):  	  	  
            x = minx + col * pixelsize  	  	  
            y = miny + row * pixelsize  	  	  
            # "Leaf" is the only well-behaved fractal - all of the others crash  	  	  
            #  	  	  
            if imagename in [ 'leaf', ]:  	  	  
                idx = PixelColorOrIndex(complex(x, y), None)  	  	  
                color = palette[idx]  	  	  
            # The rest of the fractals  	  	  
            else:  	  	  
                color = PixelColorOrIndex(complex(x, y), palette)  	  	  
            cc.append(color)  	  	  
            y = miny + row * pixelsize # prepare for next loop  	  	  
            x = minx + col * pixelsize # prepare for next loop  	  	  

        img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))  	  	  
        portion = 512 - row / 512  	  	  
        window.update()  # display a row of pixels  	  	  

        portion = 512 - row / 512 # prepare for next loop  	  	  
        # pixelsWrittenSoFar(portion, )  # This way isn't working let me try somthing eles...  	  	  
        #total_pixles = pixelsWrittenSoFar(row, col)  # will equal 262144 when the program is finished  	  	  
        print(pixelsWrittenSoFar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column  	  	  


def pixelsWrittenSoFar(rows, cols):  	  	  
    portion = (512 - rows) / 512  	  	  
    pixels = (512 - rows) * 512  	  	  
    status_percent = '{:>4.0%}'.format(portion)  	  	  
    status_bar_width = 34  	  	  
    status_bar = '=' * int(status_bar_width * portion)  	  	  
    status_bar = '{:<33}'.format(status_bar)  	  	  
    # print(f"{pixels} pixels have been output so far")  	  	  
    # return pixels  	  	  
    # return '[' + status_percent + ' ' + status_bar + ']'  	  	  
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))  	  	  


# def pixelsWrittenSoFar(rows, cols):  	  	  
#     pixels = 0  	  	  
#     for r in range(rows + 1):  	  	  
#         pixels = pixels + cols  	  	  
#     print(pixels, "pixels have been output so far", file=sys.stderr)  	  	  
#     return pixels  	  	  



# These are the different views of the Mandelbrot set you can make with this  	  	  
# program.  	  	  
#  	  	  
# For convenience I have placed these into a dictionary so you may easily  	  	  
# switch between them by entering the name of the image you want to generate  	  	  
# into the variable 'image'.  	  	  
images = {  	  	  
        'mandelbrot': {  	  	  
            'centerX': -0.6,  	  	  
            'centerY': 0.0,  	  	  
            'axisLen': 2.5,  	  	  
            },  	  	  

        'mandelbrot-zoomed': {  	  	  
            'centerX': -1.0,  	  	  
            'centerY': 0.0,  	  	  
            'axisLen': 1.0,  	  	  
            },  	  	  

        'spiral0': {  	  	  
            'centerX': -0.761335372924805,  	  	  
            'centerY': 0.0835704803466797,  	  	  
            'axisLen': 0.004978179931102462,  	  	  
            },  	  	  

        'spiral1': {  	  	  
            'centerX': -0.747,  	  	  
            'centerY': 0.1075,  	  	  
            'axisLen': 0.002,  	  	  
            },  	  	  

        'seahorse': {  	  	  
            'centerX': -0.748,  	  	  
            'centerY': -0.102,  	  	  
            'axisLen': 0.008,  	  	  
            },  	  	  

        'spiral1': {  	  	  
            'centerX': -0.747,  	  	  
            'centerY': 0.1075,  	  	  
            'axisLen': 0.002,  	  	  
            },  	  	  

        'elephants': {  	  	  
            'centerX':  0.3015,  	  	  
            'centerY':  -0.0200,  	  	  
            'axisLen':  0.03,  	  	  
            },  	  	  

        'leaf': {  	  	  
            'centerX': -1.543577002,  	  	  
            'centerY': -0.000058690069,  	  	  
            'axisLen':  0.000051248888,  	  	  
            },  	  	  

        'starfish': {  	  	  
            'centerX': -0.463595023481762,  	  	  
            'centerY': 0.598380871135558,  	  	  
            'axisLen': 0.00128413675654471,  	  	  
            },  	  	  
        }  	  	  


def mbrot_main(image):  	  	  
    global img  	  	  
    # Set up the GUI so that we can paint the fractal image on the screen  	  	  
    print("Rendering {} fractal".format(image), file=sys.stderr)  	  	  
    before = time.time()  	  	  
    global window  	  	  
    window = Tk()  	  	  
    img = PhotoImage(width=512, height=512)  	  	  
    paint(images, image, window)  	  	  

    # Save the image as a PNG  	  	  
    after = time.time()  	  	  
    print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)  	  	  
    img.write(f"{image}.png")  	  	  
    print(f"Wrote picture {image}.png", file=sys.stderr)  	  	  

    # Call tkinter.mainloop so the GUI remains open  	  	  
    print("Close the image window to exit the program", file=sys.stderr)  	  	  
    mainloop()  	  	  

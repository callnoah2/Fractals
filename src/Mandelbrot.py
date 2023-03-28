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


from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
import time

# GRAPEFRUIT_PINK = '#E8283F'
# LEMON = '#FDFF00'
# LIME_GREEN = '#89FF00'
# KUMQUAT = '#FAC309'
# MAX_ITERATIONS = -1
# POMELLO = '#2FFF00'
# TANGERINE = '#F7B604'
# WHITE = '#FFFFFF'
# CONCORD_GRAPE = '#51419C'
# PLUM = '#7D387D'
# BLACK = '#000000'

img = None

mainWindowObject = None


def mBrotIter(c, max_iterations):
    """
    Given a coordinate in the complex plane, returns the iteration count of the Mandelbrot function for that point.

    The iteration count corresponds to the number of times the function z = z^2 + c can be iteratively applied to the
    complex number z = 0 before the absolute value of z becomes greater than 2 or the maximum number of iterations
    is reached, whichever comes first.
    """
    z = 0
    for i in range(max_iterations):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iterations


# def paint(fractals, imagename, window):
#     """Paint a Fractal image into the TKinter PhotoImage canvas.
#     This code creates an image which is 640x640 pixels in size."""
#
#     global palette
#     global img
#
#     fractal = fractals[imagename]
#
#     # Figure out how the boundaries of the PhotoImage relate to coordinates on
#     # the imaginary plane.
#     minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
#     maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
#     miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
#     maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)
#
#     # Display the image on the screen
#     canvas = Canvas(window, width=512, height=512, bg='#000000')
#     canvas.pack()
#     canvas.create_image((256, 256), image=img, state="normal")
#
#     # At this scale, how much length and height on the imaginary plane does one
#     # pixel take?
#     pixelsize = abs(maxx - minx) / 512
#
#     portion = 0
#     total_pixels = 512 * 512  # 262144
#     # loop
#     for row in range(512, 0, -1):
#         cc = []
#         for col in range(512):
#             x = minx + col * pixelsize
#             y = miny + row * pixelsize
#             # "Leaf" is the only well-behaved fractal - all of the others crash
#             #
#             if imagename in [ 'leaf', ]:
#                 idx = PixelColorOrIndex(complex(x, y), None)
#                 color = palette[idx]
#             # The rest of the fractals
#             else:
#                 color = PixelColorOrIndex(complex(x, y), palette)
#             cc.append(color)
#             y = miny + row * pixelsize # prepare for next loop
#             x = minx + col * pixelsize # prepare for next loop
#
#         img.put('{' + ' '.join(cc) + '}', to=(0, 512-row))
#         portion = 512 - row / 512
#         window.update()  # display a row of pixels
#
#         portion = 512 - row / 512 # prepare for next loop
#         # pixelsWrittenSoFar(portion, )  # This way isn't working let me try somthing eles...
#         #total_pixles = pixelsWrittenSoFar(row, col)  # will equal 262144 when the program is finished
#         print(pixelsWrittenSoFar(row, col), end='\r', file=sys.stderr)  # the '\r' returns the cursor to the leftmost column


# def pixelsWrittenSoFar(rows, cols):
#     portion = (512 - rows) / 512
#     pixels = (512 - rows) * 512
#     status_percent = '{:>4.0%}'.format(portion)
#     status_bar_width = 34
#     status_bar = '=' * int(status_bar_width * portion)
#     status_bar = '{:<33}'.format(status_bar)
#     # print(f"{pixels} pixels have been output so far")
#     # return pixels
#     # return '[' + status_percent + ' ' + status_bar + ']'
#     return ''.join(list(['[', status_percent, ' ', status_bar, ']']))

# def mbrot_main(image):
#     global img
#     # Set up the GUI so that we can paint the fractal image on the screen
#     print("Rendering {} fractal".format(image), file=sys.stderr)
#     before = time.time()
#     global window
#     window = Tk()
#     img = PhotoImage(width=512, height=512)
#     paint(images, image, window)
#
#     # Save the image as a PNG
#     after = time.time()
#     print(f"\nDone in {after - before:.3f} seconds!", file=sys.stderr)
#     img.write(f"{image}.png")
#     print(f"Wrote picture {image}.png", file=sys.stderr)
#
#     # Call tkinter.mainloop so the GUI remains open
#     print("Close the image window to exit the program", file=sys.stderr)
#     mainloop()
#!/usr/bin/env python3
# Phoenix Fractal Visualizer - a variation of the Julia Fractal

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
from tkinter import Tk, Canvas, PhotoImage, mainloop
from time import time

canvasSize = 512


# def getColorFromPalette(z):
#     """
#     Return the index of the color of the current pixel
#     within the Phoenix fractal in the palette array
#     """
#     Julia = complex(0.5667, 0.0)
#
#     pheonix = complex(-0.5, 0.0)
#
#     zFlipped = complex(z.imag, z.real)
#
#     zPrev = 0+0j
#     # set Z back to zFlipped, it is literally super-important that we do this
#     # before the next part of the algorithm
#     z = zFlipped
#
#     for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?
#
#         zSave = z  # save the current Z value before we overwrite it
#         # compute the new Z value from the current and previous Zs
#         z = z * z + Julia + (pheonix * zPrev)
#         zPrev = zSave  # Set the prevZ value for the next iteration
#
#         # if the absolute value of Z is graeter or equal than 2, then return that color
#         if abs(z) > 2:
#             return grad[i]  # The sequence is unbounded
#     return grad[101]         # Else this is a bounded sequence
def phoenixIter(z, maxIter):
    """
    Return the iteration count of the Phoenix fractal for the given point in the complex plane
    """
    Julia = complex(0.5667, 0.0)
    pheonix = complex(-0.5, 0.0)

    zFlipped = complex(z.imag, z.real)
    zPrev = 0+0j
    z = zFlipped

    for i in range(maxIter):
        zSave = z
        z = z * z + Julia + (pheonix * zPrev)
        zPrev = zSave

        if abs(z) > 2:
            return i

    return maxIter

# Save_As_Picture = True
# tkPhotoImage = None

# def makePictureOfFractal(f, i, e, w, g, p, W, a, b, canvasSize):
#     """Paint a Fractal image into the TKinter PhotoImage canvas.
#     Assumes the image is 640x640 pixels."""
#
#     min = ((f['centerX'] - (f['axisLength'] / 2.0)),
#            (f['centerY'] - (f['axisLength'] / 2.0)))
#
#     max = ((f['centerX'] + (f['axisLength'] / 2.0)),
#            (f['centerY'] + (f['axisLength'] / 2.0)))
#
#     # Display the image on the screen
#     tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=canvasSize, height=canvasSize, bg=W)
#
#     # pack the canvas object into its parent widget
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()
#
#     tk_Interface_PhotoImage_canvas_pixel_object.create_image((canvasSize/2, canvasSize/2), image=p, state="normal")
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.
#
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?
#
#     size = abs(max[0] - min[0]) / canvasSize
#
#     # pack the canvas object into its parent widget
#     tk_Interface_PhotoImage_canvas_pixel_object.pack()
#
#     row = canvasSize
#     while row in range(canvasSize, 0, -1):
#         # for c (c == column) in the range of pixels in a square of size s
#         cs = []
#         for c in range(canvasSize):
#             X = min[0] + c * size
#             Y = 0
#             cp = getColorFromPalette(complex(X, Y))
#             cs.append(cp)
#         pixls = '{' + ' '.join(cs) + '}'
#         p.put(pixls, (0, canvasSize - row))
#         w.update()  # display a row of pixels
#         fraction_of_pixels_writtenSoFar = (canvasSize - row) / canvasSize # update the number of pixels output so far
#         # print a statusbar on the console
#         print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"
#                 + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",
#                 end="\r"  # the end
#                 , file=sys.stderr)
#         row -= 1

# BLACK = '#FFFFFF'
# # grad += [BLACK] * 6  # six pixels should be enough
#
# # This is how you write colors for computers
# WHITE = '#ffffff'  # white
# RED = '#ff0000'  # red
# BLUE = '#00ff00'  # blue
# GREEN = '#0000ff'  # green
# # BLACK = '#000000'  # black
# ORANGE = '#ffa50'  # orange
# TOMATO = '#ff6347'  # tomato (a shade of red)
# HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)
# REBECCA_PURPLE = '#663399'  # Rebecca Purple
# LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)
# GREY0 = '#000000'  # gray 0 - basically the same as black
# GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36
# GREY74 = '#bdbdbd'  # gray 74 - almost white
# GRAY99 = '#fcfcfc'  # gray 99 - almost white


# def phoenix_main(i):
#     """The main entry-point for the Phoenix fractal generator"""
#     global win
#
#     b4 = time()
#
#     win = Tk()
#
#     print("Rendering %s fractal" % i, file=sys.stderr)
#     # construct a new TK PhotoImage object that is 512 pixels square...
#     tkPhotoImage = PhotoImage(width=canvasSize, height=canvasSize)
#     makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, None, None, canvasSize)
#
#     if Save_As_Picture:
#         # Write out the Fractal into a .gif image file
#         tkPhotoImage.write(i + ".png")
#         #tkPhotoImage.write(f"{i}.png")
#         print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)
#         print("Wrote picture " + i + ".png", file=sys.stderr)
#
#     print("Close the image window to exit the program", file=sys.stderr)
#     # Call tkinter.mainloop so the GUI remains open
#     mainloop()

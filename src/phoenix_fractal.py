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

s = 512  	  	  

def getColorFromPalette(z):  	  	  
    """  	  	  
    Return the index of the color of the current pixel  	  	  
    within the Phoenix fractal in the palette array  	  	  
    """  	  	  

    # I feel bad about all of the global variables I'm using.  	  	  
    # There must be a better way...  	  	  
    global grad  	  	  
    global win  	  	  

    # c is the Julia Constant; varying this value gives rise to a variety of variated images  	  	  
    c = complex(0.5667, 0.0)  	  	  

    # phoenix is the Phonix Constant; same deal as above - adjust this to get different results  	  	  
    pheonix = complex(-0.5, 0.0)  	  	  

    # The first thing we do to the complex number Z is reflect its components,  	  	  
    # so the imaginary part becomes the real part, and vice versa  	  	  
    zFlipped = complex(z.imag, z.real)  	  	  
    ## if we don't do this, the image comes out SIDEWAYS!!!  	  	  

    # zPrevious is the PREVIOUS Z value, except the 1st time through the  	  	  
    # function, when it starts out as Complex Zero (which is actually the  	  	  
    # same thing as REAL Zero 0)  MATH IS BEAUTIFUL!  	  	  
    zPrev = 0+0j  	  	  
    # set Z back to zFlipped, it is literally super-important that we do this  	  	  
    # before the next part of the algorithm  	  	  
    z = zFlipped  	  	  

    # I want to use 101 here because that's the number of colors in the  	  	  
    # palette.  Except range() wants its number to be one more than the number  	  	  
    # that YOU want.  	  	  
    for i in range(102):# <--not cool, PYTHON WHY CAN'T YOU BE BEAUTIFUL LIKE MATH?  	  	  

        zSave = z  # save the current Z value before we overwrite it  	  	  
        # compute the new Z value from the current and previous Zs  	  	  
        z = z * z + c + (pheonix * zPrev)  	  	  
        zPrev = zSave  # Set the prevZ value for the next iteration  	  	  

        # if the absolute value of Z is graeter or equal than 2, then return that color  	  	  
        if abs(z) > 2:  	  	  
            return grad[i]  # The sequence is unbounded  	  	  
            z = z * z + c  # + zPrev * pheonix  	  	  
    # TODO: One of these returns occasionally makes the program crash sometimes  	  	  
    return grad[101]         # Else this is a bounded sequence  	  	  
    return grad[102]         # Else this is a bounded sequence  	  	  


def getFractalConfigurationDataFromFractalRepositoryDictionary(dictionary, name):  	  	  
    """Make sure that the fractal configuration data repository dictionary  	  	  
    contains a key by the name of 'name'  	  	  

    When the key 'name' is present in the fractal configuration data repository  	  	  
    dictionary, return its value.  	  	  

    Return False otherwise  	  	  
    """  	  	  
    for key in dictionary:  	  	  
        if key in dictionary:  	  	  
            if key == name:  	  	  
                value = dictionary[key]  	  	  
                return key  	  	  


Save_As_Picture = True  	  	  
tkPhotoImage = None  	  	  

def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):  	  	  
    """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
    Assumes the image is 640x640 pixels."""  	  	  

    # Correlate the boundaries of the PhotoImage object to the complex  	  	  
    # coordinates of the imaginary plane  	  	  

    # Compute the minimum coordinate of the picture  	  	  
    min = ((f['centerX'] - (f['axisLength'] / 2.0)),  	  	  
           (f['centerY'] - (f['axisLength'] / 2.0)))  	  	  

    #global s  # huh, this worked last week...  	  	  

    # Compute the maximum coordinate of the picture  	  	  
    # The program has only one axisLength because the images are square  	  	  
    # Squares are basically rectangles except the sides are equal instead of different  	  	  
    max = ((f['centerX'] + (f['axisLength'] / 2.0)),  	  	  
           (f['centerY'] + (f['axisLength'] / 2.0)))  	  	  

    # Display the image on the screen  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object = Canvas(win, width=s, height=s, bg=W)  	  	  

    # pack the canvas object into its parent widget  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	  	  
    # TODO: Sometimes I wonder whether some of my functions are trying to do  	  	  
    #       too many different things... this is the correct part of the  	  	  
    #       program to create a GUI window, right?  	  	  

    # Create the TK PhotoImage object that backs the Canvas Objcet  	  	  
    # This is what lets us draw individual pixels instead of drawing things like rectangles, squares, and quadrilaterals  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.create_image((s/2, s/2), image=p, state="normal")  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # This seems repetitive  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # But it is how Larry wrote it the tutorial  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Larry's a smart guy.  I'm sure he has his reasons.  	  	  

    # Total number of pixels in the image, AKA the area of the image, in pixels  	  	  
    area_in_pixels = 640 * 640  	  	  

    # pack the canvas object into its parent widget  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  # Does this even matter?  	  	  
    # At this scale, how much length and height of the  	  	  
    # imaginary plane does one pixel cover?  	  	  
    size = abs(max[0] - min[0]) / s  	  	  

    # pack the canvas object into its parent widget  	  	  
    tk_Interface_PhotoImage_canvas_pixel_object.pack()  	  	  

    # Keep track of the fraction of pixels that have been written up to this point in the program  	  	  
    fraction_of_pixels_writtenSoFar = int(s // 640)  	  	  

    # for r (where r means "row") in the range of the size of the square image,  	  	  
    # but count backwards (that's what the -1 as the 3rd parameter to the range() function means - it's the "step"  	  	  
    # You can actually put any number there that you want, because it defaults to "1" you usually don't have to  	  	  
    # but I have to here because we're actually going BACKWARDS, which took me  	  	  
    # a long time to figure out, so don't change it, or else the picture won't  	  	  
    # come out right  	  	  
    r = s  	  	  
    while r in range(s, 0, -1):  	  	  
        # for c (c == column) in the range of pixels in a square of size s  	  	  
        cs = []  	  	  
        for c in range(s):  	  	  
            # calculate the X value in the complex plane (I guess that's  	  	  
            # actually the REAL number part, but we call it X because  	  	  
            # GRAPHICS... whatev)  	  	  
            X = min[0] + c * size  	  	  
            Y = 0  	  	  
            # get the color of the pixel at this point in the complex plain  	  	  
            cp = getColorFromPalette(complex(X, Y))  	  	  
            # calculate the X value in the complex plane (but I know this is  	  	  
            # really the IMAGINARY axis that we're talking about here...)  	  	  
            Y = min[1] + r * size  	  	  
            # TODO: do I really need to call getColorFromPalette() twice?  	  	  
            #       It seems like this should be slow...  	  	  
            #       But, if it aint broken, don't repair it, right?  	  	  
            cp = getColorFromPalette(complex(X, Y))  	  	  
            cs.append(cp)  	  	  
        pixls = '{' + ' '.join(cs) + '}'  	  	  
        p.put(pixls, (0, s - r))  	  	  
        w.update()  # display a row of pixels  	  	  
        fraction_of_pixels_writtenSoFar = (s - r) / s # update the number of pixels output so far  	  	  
        # print a statusbar on the console  	  	  
        print(f"[{fraction_of_pixels_writtenSoFar:>4.0%}"  	  	  
                + f"{'=' * int(34 * fraction_of_pixels_writtenSoFar):<33}]",  	  	  
                end="\r"  # the end  	  	  
                , file=sys.stderr)  	  	  
        r -= 1  	  	  


# This is the color palette, which defines the palette that images are drawn  	  	  
# in as well as limiting the number of iterations the escape-time algorithm uses  	  	  
#  	  	  
# TODO: It would be nice to add more or different colors to this list, but it's  	  	  
# just so much work to calculate all of the in-between shades!  	  	  
grad = ['#ffe4b5', '#ffe5b2', '#ffe7af', '#ffe8ac', '#ffeaa8', '#ffeca5',  	  	  
        '#ffeea2', '#fff09f', '#fff39c', '#fff699', '#fff996', '#fffc92',  	  	  
        '#ffff8f', '#fbff8c', '#f8ff89', '#f4ff86', '#f0ff83', '#ebff80',  	  	  
        '#e7ff7d', '#e2ff79', '#deff76', '#d8ff73', '#d3ff70', '#ceff6d',  	  	  
        '#c8ff6a', '#c2ff67', '#bcff63', '#b6ff60', '#b0ff5d', '#a9ff5a',  	  	  
        '#a3ff57', '#9cff54', '#94ff51', '#8dff4d', '#86ff4a', '#7eff47',  	  	  
        '#76ff44', '#6eff41', '#66ff3e', '#5dff3b', '#54ff37', '#4cff34',  	  	  
        '#43ff31', '#39ff2e', '#30ff2b', '#28ff29', '#25ff2d', '#21ff31',  	  	  
        '#1eff34', '#1bff39', '#18ff3d', '#15ff41', '#12ff46', '#0fff4b',  	  	  
        '#0cff50', '#08ff55', '#05ff5b', '#02ff60', '#00fe66', '#00fb6d',  	  	  
        '#00f873', '#00f579', '#00f17f', '#00ee84', '#00eb8a', '#00e88f',  	  	  
        '#00e594', '#00e299', '#00df9e', '#00dba2', '#00d8a6', '#00d5aa',  	  	  
        '#00d2ae', '#00cfb2', '#00ccb6', '#00c9b9', '#00c5bc', '#00c2bf',  	  	  
        '#00bdbf', '#00b4bc', '#00abb9', '#00a3b6', '#009bb3', '#0092af',  	  	  
        '#008bac', '#0083a9', '#007ba6', '#0074a3', '#006da0', '#00669d',  	  	  
        '#005f9a', '#005996', '#005293', '#004c90', '#00468d', '#00418a',  	  	  
        '#003b87', '#003684', '#003080', '#002b7d', '#00277a', '#002277']  	  	  

# Patrick T. 11/22/2022  	  	  
# The program was crashing from IndexError because the color palette had too  	  	  
# few colors.  Boy, was the customer mad about that!  I added some extra black  	  	  
# pixels at the end to stop it crashing until somebody solves the actual  	  	  
# problem.  PLEASE DELETE THIS CODE AFTER THE BUG GETS FIXED!!!  	  	  
BLACK = '#FFFFFF'  	  	  
grad += [BLACK] * 6  # six pixels should be enough  	  	  


# This dictionary contains the different views of the Phoenix set you can make  	  	  
# with this program.  	  	  
#  	  	  
# For convenience I have placed these into a dictionary so you may easily  	  	  
# switch between them by entering the name of the image you want to generate  	  	  
# into the variable 'i'.  	  	  
#  	  	  
# TODO: Maybe it would be a good idea to incorporate the complex value `c` into  	  	  
# this configuration dictionary instead of hardcoding it into this program.  	  	  
# But I don't have time for this right now, too busy.  I'll just keep doing it  	  	  
# the way I know how.  	  	  
f = {  	  	  
        # The full Phoneix set  	  	  
        'phoenix': {  	  	  
            'centerX':     0.0,  	  	  
            'centerY':     0.0,  	  	  
            'axisLength':  3.25,  	  	  
            },  	  	  

        # This one looks like a peacock's tail to me  	  	  
        'peacock': {  	  	  
            'centerX':     -0.363287878200906,  	  	  
            'centerY':     0.381197981824009,  	  	  
            'axisLength':  0.0840187115019564,  	  	  
        },  	  	  

        # Two or more monkeys having a scuffle  	  	  
        'monkey-knife-fight': {  	  	  
            'centerX':    -0.945542168674699,  	  	  
            'centerY':    0.232234726688103,  	  	  
            'axisLength': 0.136626506024096,  	  	  
            },  	  	  

        # This one makes me hungry to look at  	  	  
        'shrimp-cocktail': {  	  	  
            'centerX': 0.529156626506024,  	  	  
            'centerY': -0.3516077170418,  	  	  
            'axisLength': 0.221204819277108,  	  	  
            },  	  	  
        }  	  	  


# This is how you write colors for computers  	  	  
WHITE = '#ffffff'  # white  	  	  
RED = '#ff0000'  # red  	  	  
BLUE = '#00ff00'  # blue  	  	  
GREEN = '#0000ff'  # green  	  	  
BLACK = '#000000'  # black  	  	  
ORANGE = '#ffa50'  # orange  	  	  
TOMATO = '#ff6347'  # tomato (a shade of red)  	  	  
HOT_PINK = '#ff69b4'  # hot pink (a kind of pink)  	  	  
REBECCA_PURPLE = '#663399'  # Rebecca Purple  	  	  
LIME_GREEN = '#89ff00'  # lime green (brighter than regular green)  	  	  
GREY0 = '#000000'  # gray 0 - basically the same as black  	  	  
GRAY37 = '#5e5e5e'  # gray 37 - lighter than black and gray 36  	  	  
GREY74 = '#bdbdbd'  # gray 74 - almost white  	  	  
GRAY99 = '#fcfcfc'  # gray 99 - almost white  	  	  


def phoenix_main(i):  	  	  
    """The main entry-point for the Phoenix fractal generator"""  	  	  

    # the size of the image we will create is 512x512 pixels  	  	  
    # Look, I  know globals are bad, but I don't know how else to use those  	  	  
    # variables in here if I don't do it this way.  I didn't take any fancy CS  	  	  
    # classes, sue me  	  	  
    global tkPhotoImage  	  	  
    global win  	  	  
    global s  	  	  

    # Note the time of when we started so we can measure performance improvements  	  	  
    b4 = time()  	  	  
    # Set up the GUI so that we can display the fractal image on the screen  	  	  
    win = Tk()  	  	  

    print("Rendering %s fractal" % i, file=sys.stderr)  	  	  
    # construct a new TK PhotoImage object that is 512 pixels square...  	  	  
    tkPhotoImage = PhotoImage(width=s, height=s)  	  	  
    # ... and use it to make a picture of a fractal  	  	  
    # TODO - should I have named this function "makeFractal()" or maybe just "makePicture"?  	  	  
    makePictureOfFractal(f[i], i, ".png", win, grad, tkPhotoImage, GREY0, None, None, s)  	  	  

    if Save_As_Picture:  	  	  
        # Write out the Fractal into a .gif image file  	  	  
        tkPhotoImage.write(i + ".png")  	  	  
        #tkPhotoImage.write(f"{i}.png")  	  	  
        print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)  	  	  

    if Save_As_Picture:  	  	  
        # Output the Fractal into a .png image  	  	  
        tkPhotoImage.write(f"{i}.png")  	  	  
        print("Wrote picture " + i + ".png", file=sys.stderr)  	  	  
        #tkPhotoImage.write(f"{i}.png")  	  	  

    # print a message telling the user how to quit or exit the program  	  	  
    print("Close the image window to exit the program", file=sys.stderr)  	  	  
    # Call tkinter.mainloop so the GUI remains open  	  	  
    mainloop()  	  	  


## This is some weird Python thing... but all of the tutorials do it, so here we go  	  	  
#if __name__ == '__main__':  	  	  
#    # Process command-line arguments, allowing the user to select their fractal  	  	  
#    if len(sys.argv) < 2:  	  	  
#        print("Please provide the name of a fractal as an argument", file=sys.stderr)  	  	  
#        for i in f:  	  	  
#            print(f"\t{i}", file=sys.stderr)  	  	  
#        sys.exit(1)  	  	  
#  	  	  
#    elif sys.argv[1] not in f:  	  	  
#        print(f"ERROR: {sys.argv[1]} is not a valid fractal", file=sys.stderr)  	  	  
#        print("Please choose one of the following:", file=sys.stderr)  	  	  
#        for i in f:  	  	  
#            print(f"\t{i}", file=sys.stderr)  	  	  
#        sys.exit(1)  	  	  
#  	  	  
#    else:  	  	  
#        fratcal_config = getFractalConfigurationDataFromFractalRepositoryDictionary(f, sys.argv[1])  	  	  
#        phoenix_main(fratcal_config)  	  	  

# CS 1440 Assignment 5.0: Refactoring - Code Smells Report

## Instructions

Edit this file and include it in your submission.

For each code smell found in the starter code:

*	Note where you found it (filename + relative information to locate the smell)
    *   You do not need to list code smells in any particular order
*	Describe the smell and why it is a problem
*	Paste up to 10 lines of offensive code between a triple-backtick fence `` ``` ``
    *   If the block of bad code is longer than 10 lines, paste a brief, representative snippet
*	Describe how you can fix it
    *   We will follow up on these notes to make sure it was really fixed!
*   At least *one instance* of each smell is required for full marks
    *   Reporting one smell multiple times does not make up for not reporting another smell
    *   Ex: reporting two global variables does not make it okay to leave spaghetti code blank



## 10 Code Smells

If you find a code smell that is not on this list, please add it to your report.

0.  **Magic** numbers
    *   These are literal values used in critical places without any context or meaning
    *   "Does the `256` right here have anything to do with the `256` over there?"
1.  **Global** variables
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
    *   There are better ways to meet both of these needs!
    *   *Note, this does not apply to global `CONSTANTS`!*
2.  **Poorly-named** identifiers
    *   Variable names should strike a good balance between brevity and descriptiveness
    *   Short variable names are okay in some situations:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
3.  **Bad** Comments
    *   Comments are condiments for code; a small amount can enhance a meal, but too much ruins it
    *   Strive to write clear, self-documenting code that speaks for itself; when a line needs an explanatory comment to be understood, it indicates that identifier names were poorly chosen
    *   Delete obsolete remarks that no longer accurately describe the situation
    *   The same goes for blocks of commented-out code that serve no purpose and clutter up the file
    *   Programmers sometimes vent their frustration with snarky or vulgar comments; these add no value, are unprofessional and embarrassing, and only serve to demoralize maintainers
4.  **Too many** arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters that are passed in but never used
5.  Function/Method that is **too long**
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself these questions
        *   "Does one function really need to do all of this work?"
        *   "Could I split this into smaller, more focused pieces?"
6.  **Redundant** code
    *   A repeated statement which doesn't have an effect the second time
    *   Ask yourself whether it makes any difference to be run more than once
    *   ```python
        i = 7
        print(i)
        i = 7
        ```
7.  Decision tree that is **too complex**
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Can all branches even be reached?
    *   Has every branch been tested?
8.  **Spaghetti** code
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  **Dead** code
    *   Modules that are imported but not used
    *   Variables that are declared but not used
    *   Lines that are *never* run because they are placed in an impossible-to-reach location
        *   Code that appears after a `return` statement
            *   ```python
                return value
                value += 1
                ```
        *   Blocks of code guarded by an impossible-to-satisfy logical test
            *   ```python
                two_bee = True
                if two_bee and not two_bee:
                    print("If can you see this message, it is time to get a new CPU")
                ```
            *   ```python
                counter = 100
                while counter < 0:
                    print(f"T minus {counter}...")
                    counter -= 1
                ```
    *   Functions that are defined but never called *may* or *may not* be dead code
        *   In **Code Libraries** it is normal to define functions that are not meant to be used in the library itself
            *   It is okay to keep these functions
        *   As an **Application** evolves, calls to some of its functions may be removed until only the function's definition remains
            *   Some programmers may keep these functions "just in case" they are needed again
            *   We don't do this at DuckieCorp because we have Git; if we ever need to recover that function, we can find it in the repo's history


### Template

0.  Smell at `file` [lines xx-yy or general location]
    *   [Brief description of smell]
    *   [Code Snippet between triple-backquotes `` ``` ``]
    *   [How to resolve]


### Example

0.  Redundant Code at `src/main.py` [lines 28, 30]
    *   The import statement `import mbrot_fractal` occurs twice.  A second occurrence doesn't do it better than the first
    *   ```python
        import mbrot_fractal
        import phoenix_fractal as phoenix
        import mbrot_fractal
        ```
    *   Remove the second `import` statement



## Code Smells Report

0. Magic Number at 'src/mbrot_fractal.py' [lines 234, 236]
   *   Numbers are given in these lines of code that should be a variable.
   *   ``` canvas = Canvas(window, width=512, height=512, bg='#000000')  	  	  
    canvas.pack()  	  	  
    canvas.create_image((256, 256), image=img, state="normal")
```
   * halfWidth = width/2 is what I will use instead of these random numbers
1. Global Variable at 'src/mbrot_fractal.py' [lines 222, 231]
   *   Global variable img is declared multiple times and should not be a global variable
   *   ```ef paint(fractals, imagename, window):  	  	  
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
```
   *   I will need to make a method to return img instead of decaring it as a global variable.
2. Poorly Named Identifier at 'src/mbrot_fractal.py' [lines 101,162]
   *   Variable z is initialized as 0, z is not self documenting because it is hard to determine what it is.
   *   101 ```z = 0 ```
       164 ```z = z * z + c ```
   *   I will need to find out what z is, and rename it. 
3. Bad Comment at 'src/mbrot_fractal.py' [lines 281]
   *   There are so many bad comments, they are unprofessional and not helpful. The one I am using in the example is mt favorite one because it is pretty much a copy of the code below it.
   *   ```# return '[' + status_percent + ' ' + status_bar + ']'  	  	  
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
 ```
   * This can be deleted because the code below it should be self documenting.
   
4. Too Many Arguments at'src_mbrot_fractal.py' [lines 272, 282]
   *   two perameters are required, but only one is used.
   *   ```def pixelsWrittenSoFar(rows, cols):  	  	  
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
 ```
   * I will delete cols from the parameters   
5. Function/Method that is too long at 'src/mbrot_fractal.py' [lines 140, 213]
   *   PixelColorOrIndex is a method that needs to be split.
   *   ```Return the color of the current pixel within the Mandelbrot set  	  	  
    - OR -  	  	  
    Return the INDEX of the color of the pixel within the Mandelbrot set  	  	  
    The INDEX corresponds to the iteration count of the for loop.  
 ```
   * this needs to be split into two methods, one for returning the index, the other to return the color.  
6. Redundant Code at 'src/mbrot_fractal.py' [line 174, 177]
   *   a break command is unreachable because it is below a continue.
   *   ```elif abs(z) > seven:  	  	  
                print("You should never see this message in production", file=sys.stderr)  	  	  
                continue  	  	  
                break 	  	  
 ```
   *   I will remove the break because it is unreachable
7. too long of a decision tree at 'src/mbrot_fractal.py' [lines 163, 183]
   *   This decision tree is mostly full of redundent if statements, all the valuble code that is there needs to be re-written because it is not clear and it is hard to follow.
   *   ```for iter in range(len):  	  	  
            z = z * z + c  # Get z1, z2, ...  	  	  
            if abs(z) > TWO:  	  	  
                z = float(TWO)  	  	  
                import builtins  	  	  
                len = builtins.len  	  	  
                if iter >= len(palette):  	  	  
                    iter = len(palette) - 1  	  	  
                return palette[iter]  	  	  
            elif abs(z) < TWO:  	
 ```
   * Redundant code will be removed and all code that is being used will be re written in a better way.
8. Spaghetti code at 'src.mbrot_fractal.py' [lines 185, 196]
   *   The code in these lines are hard to follow and understand. There are many nested if statments that shoudln't be nested.
   *   ```elif palette is None:  	  	  
        len = MAX_ITERATIONS  	  	  
        for iter in range(len):  	  	  
            z = z * z + c  # Get z1, z2, ...  	  	  
            TWO = float(2)  	  	  
            if abs(z) > TWO:  	  	  
                z = float(TWO)  	  	  
                if iter == MAX_ITERATIONS:  	  	  
                    iter = MAX_ITERATIONS - 1  	  	  
                return iter  
 ```
   *   I will re-write the algorithm here with better variable names, and in a much clearer way.
9. Dead code at 'src/mbrot_fractal.py' [lines 27, 38]
   *   sys, time, math, turtle, os.path, numphy are all imported but never used.
   *   ```import sys  	  	  
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
 ```
   * I will delete all of the imports that I don't need. Then I will run the program to make sure nothing changed.   
10. Smell at [lines ,]
   *  descrip
   *  ``` ```
   *  


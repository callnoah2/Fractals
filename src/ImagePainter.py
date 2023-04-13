from tkinter import Tk, Canvas, PhotoImage, mainloop
import time
import PaletteFactory
import sys


def pixSoFar(canvas_size, row):
    fraction_of_pixels_written_so_far = (canvas_size - row) / canvas_size
    print(f"[{fraction_of_pixels_written_so_far:>4.0%}" + f"{'=' * int(34 * fraction_of_pixels_written_so_far):<33}]",
          end="\r", file=sys.stderr)
    return fraction_of_pixels_written_so_far * 100
def make_picture_of_fractal(fractalInfo, Fractal, paletteName, FractalName):

    # Setting up the tk
    centerX = fractalInfo['centerx']
    centerY = fractalInfo['centery']
    axisLen = fractalInfo['axislength']
    canvas_size = fractalInfo['pixels']
    maxIter = fractalInfo['iterations']
    # creal = fractalInfo['creal']
    # cimag = fractalInfo['cimag']
    palette = PaletteFactory.makePalette(paletteName, maxIter)
    root = Tk()
    photo_image = PhotoImage(master=root, width=canvas_size, height=canvas_size)
    min_coord = (centerX - axisLen / 2.0), (centerY - axisLen / 2.0)
    max_coord = (centerX + axisLen / 2.0), (centerY + axisLen / 2.0)

    bg_color = '#ffffff'
    canvas = Canvas(root, width=canvas_size-3, height=canvas_size-3, bg=bg_color)
    canvas.pack()
    canvas.create_image((canvas_size / 2, canvas_size / 2), image=photo_image, state="normal")
    canvas.pack()

    size = abs(max_coord[0] - min_coord[0]) / canvas_size
    start = time.time()
    row = canvas_size

    while row in range(canvas_size, 0, -1):
        cs = []
        for col in range(canvas_size):
            X = min_coord[0] + col * size
            Y = min_coord[1] + row * size

            cp = Fractal.count(Fractal, (complex(X,Y)), maxIter)
            color = palette.getColor(cp)
            cs.append(color)
        pixels = '{' + ' '.join(cs) + '}'
        photo_image.put(pixels, (0, canvas_size - row))
        root.update()
        pixSoFar(canvas_size, row)
        row -= 1
    # Save Image
    file_name = FractalName
    photo_image.write(file_name, format="png")
    # finish messages
    print(f"\nDone in {time.time() - start:.3f} seconds!", file=sys.stderr)
    print("Wrote picture " + file_name + ".png", file=sys.stderr)
    print("Close the image window to exit the program", file=sys.stderr)
    mainloop()

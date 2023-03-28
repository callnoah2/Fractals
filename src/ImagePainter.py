from tkinter import Tk, Canvas, PhotoImage
import time
import Mandelbrot
import Phoenix
import sys
import Palette
start = time.time()
maxIter = 115

# def getMin():
#     pass
# def create_window():
#     """Create and return a Tk window"""
#     win = Tk()
#     return win
#
# def create_photoimage(size):
#     """Create and return a PhotoImage object with the given size"""
#     return PhotoImage(width=size, height=size)
#
# def paint_pixel(photoimage, x, y, color):
#     """Paint a pixel with the given color at (x, y) on the given PhotoImage"""
#     photoimage.put(color, (x, y))
#
# def save_as_png(photoimage, filename):
#     """Save the given PhotoImage as a PNG file with the given filename"""
#     after = time.time()
#     print(f"\nDone in {after - start:.3f} seconds!")
#     photoimage.write(filename, format='png')
#     print(f"Wrote picture {filename}.png")
#
# def pixelsWrittenSoFar(rows, size):
#     portion = (size - rows) / size
#     status_percent = '{:>4.0%}'.format(portion)
#     status_bar_width = 34
#     status_bar = '=' * int(status_bar_width * portion)
#     status_bar = '{:<33}'.format(status_bar)
#     return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
def make_picture_of_fractal(fractal, canvas_size, fractalInfo):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    Assumes the image is 640x640 pixels."""
    root = Tk()
    photo_image = PhotoImage(master=root, width=canvas_size, height=canvas_size)
    min_coord = (fractal['centerX'] - (fractal['axisLength'] / 2.0), fractal['centerY'] - (fractal['axisLength'] / 2.0))
    max_coord = (fractal['centerX'] + (fractal['axisLength'] / 2.0), fractal['centerY'] + (fractal['axisLength'] / 2.0))

    bg_color = '#ffffff'
    canvas = Canvas(root, width=canvas_size, height=canvas_size, bg=bg_color)
    canvas.pack()
    canvas.create_image((canvas_size / 2, canvas_size / 2), image=photo_image, state="normal")
    canvas.pack()

    area_in_pixels = 640 * 640
    size = abs(max_coord[0] - min_coord[0]) / canvas_size

    row = canvas_size
    while row in range(canvas_size, 0, -1):
        cs = []
        for col in range(canvas_size):
            X = min_coord[0] + col * size
            Y = min_coord[1] + row * size
            cp = Phoenix.phoenixIter(complex(X, Y),maxIter)
            color = Palette.getColor(cp)
            cs.append(color)
        pixels = '{' + ' '.join(cs) + '}'
        photo_image.put(pixels, (0, canvas_size - row))
        root.update()
        fraction_of_pixels_written_so_far = (canvas_size - row) / canvas_size
        print(f"[{fraction_of_pixels_written_so_far:>4.0%}" + f"{'=' * int(34 * fraction_of_pixels_written_so_far):<33}]", end="\r", file=sys.stderr)
        row -= 1
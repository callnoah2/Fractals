from tkinter import Tk, Canvas, PhotoImage
import time

start = time.time()
def create_window():
    """Create and return a Tk window"""
    win = Tk()
    return win

def create_photoimage(size):
    """Create and return a PhotoImage object with the given size"""
    return PhotoImage(width=size, height=size)

def paint_pixel(photoimage, x, y, color):
    """Paint a pixel with the given color at (x, y) on the given PhotoImage"""
    photoimage.put(color, (x, y))

def save_as_png(photoimage, filename):
    """Save the given PhotoImage as a PNG file with the given filename"""
    after = time.time()
    print(f"\nDone in {after - start:.3f} seconds!")
    photoimage.write(filename, format='png')
    print(f"Wrote picture {filename}.png")

def pixelsWrittenSoFar(rows, size):
    portion = (size - rows) / size
    status_percent = '{:>4.0%}'.format(portion)
    status_bar_width = 34
    status_bar = '=' * int(status_bar_width * portion)
    status_bar = '{:<33}'.format(status_bar)
    return ''.join(list(['[', status_percent, ' ', status_bar, ']']))
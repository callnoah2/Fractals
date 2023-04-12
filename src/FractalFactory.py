import Fractal, Julia, Burningship, Mandelbrot, Mandelbrot3, Mandelbrot4, Newton, Spider, Phoenix
def makeFractal(fractalInfo):
    type = fractalInfo['type']
    centerX = fractalInfo['centerX']
    centerY = fractalInfo['centerY']
    axisLength = fractalInfo['axisLength']
    pixels = fractalInfo['pixels']
    iterations = fractalInfo['iterations']
    creal = fractalInfo['creal']
    cimag = fractalInfo['cimag']

    if type == 'mandelbrot':
        fractal = Mandelbrot()
    elif type == 'phoenix':
        fractal = Phoenix()
    elif type == 'burningshipjulia':
        fractal = Burningship()
    elif type == 'burningship':
        fractal = Burningship()
    elif type == 'spider':
        fractal = Spider()
    elif type == 'julia':
        fractal = Julia()
    elif type == 'mandelbrot3':
        fractal = Mandelbrot3()
    elif type == 'mandelbrot4':
        fractal = Mandelbrot4()
    elif type == 'newton':
        fractal = Newton()
    else:
        raise ValueError(f"Unsupported fractal type: {type}")

    return fractal
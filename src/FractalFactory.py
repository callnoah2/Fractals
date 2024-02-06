def makeFractal(fractalInfo):
    import Fractal
    from Julia import JuliaFrac
    from Burningship import BurningshipFrac
    from Mandelbrot import MandelbrotFrac
    from Mandelbrot3 import Mandelbrot3Frac
    from Mandelbrot4 import Mandelbrot4Frac
    from Newton import NewtonFrac
    from Spider import SpiderFrac
    from Phoenix import PhoenixFrac

    type = fractalInfo['type']

    if type == 'mandelbrot':
        fractal = MandelbrotFrac
    elif type == 'phoenix':
        fractal = PhoenixFrac
    elif type == 'burningshipjulia':
        fractal = BurningshipFrac
    elif type == 'burningship':
        fractal = BurningshipFrac
    elif type == 'spider':
        fractal = SpiderFrac
    elif type == 'julia':
        fractal = JuliaFrac
    elif type == 'mandelbrot3':
        fractal = Mandelbrot3Frac
    elif type == 'mandelbrot4':
        fractal = Mandelbrot4Frac
    elif type == 'newton':
        fractal = NewtonFrac
    else:
        raise ValueError(f"Unsupported fractal type: {type}")

    return fractal
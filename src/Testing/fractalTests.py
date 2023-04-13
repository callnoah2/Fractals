import unittest
import FractalParser
from Fractal import Fractal
from Mandelbrot import MandelbrotFrac
from Phoenix import PhoenixFrac
from Spider import SpiderFrac
from Julia import JuliaFrac
from Newton import NewtonFrac
parse = FractalParser.parse
class TestFractal(unittest.TestCase):
    def test_Phoenix(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        Fractal = MandelbrotFrac
        maxIter = 65
        self.assertEqual(Fractal.count(None, complex(0, 0), maxIter), 65)
        self.assertEqual(Fractal.count(None, complex(-0.751, 1.1075), maxIter), 2)
        self.assertEqual(Fractal.count(None, complex(-0.2, 1.1075), maxIter), 9)
        self.assertEqual(Fractal.count(None, complex(-0.750, 0.1075), maxIter), 30)
        self.assertEqual(Fractal.count(None, complex(-0.748, -0.1075), maxIter), 56)

    def test_Mandelbrot(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""
        # test the pixel color...
        Fractal = PhoenixFrac
        maxIter = 115
        self.assertEqual(Fractal.count(None, complex(0, 0), maxIter), 5)
        self.assertEqual(Fractal.count(None, complex(-0.751, 1.1075), maxIter), 0)
        self.assertEqual(Fractal.count(None, complex(-0.2, 1.1075), maxIter), 1)
        self.assertEqual(Fractal.count(None, complex(-0.750, 0.1075), maxIter), 34)
        self.assertEqual(Fractal.count(None, complex(-0.748, -0.1075), maxIter), 115)

    def test_SpiderColor(self):
        Fractal = SpiderFrac
        maxIter = 115
        self.assertEqual(Fractal.count(None, complex(0, 0), maxIter), 115)
        self.assertEqual(Fractal.count(None, complex(-0.751, 1.1075), maxIter), 3)
        self.assertEqual(Fractal.count(None, complex(-0.2, 1.1075), maxIter), 3)
        self.assertEqual(Fractal.count(None, complex(-0.750, 0.1075), maxIter), 115)
        self.assertEqual(Fractal.count(None, complex(-0.748, -0.1075), maxIter), 115)


    def test_Julia(self):
        Fractal = JuliaFrac
        maxIter = 115
        self.assertEqual(Fractal.count(None, complex(0, 0), maxIter), 115)
        self.assertEqual(Fractal.count(None, complex(-0.751, 1.1075), maxIter), 1)
        self.assertEqual(Fractal.count(None, complex(-0.2, 1.1075), maxIter), 2)
        self.assertEqual(Fractal.count(None, complex(-0.750, 0.1075), maxIter), 115)
        self.assertEqual(Fractal.count(None, complex(-0.748, -0.1075), maxIter), 115)

    def test_Newton(self):
        Fractal = NewtonFrac
        maxIter = 115
        self.assertEqual(Fractal.count(None, complex(0, 0), maxIter), 0)
        self.assertEqual(Fractal.count(None, complex(-0.751, 1.1075), maxIter), 3)
        self.assertEqual(Fractal.count(None, complex(-0.2, 1.1075), maxIter), 3)
        self.assertEqual(Fractal.count(None, complex(-0.750, 0.1075), maxIter), 10)
        self.assertEqual(Fractal.count(None, complex(-0.748, -0.1075), maxIter), 9)

    def test_badInput(self):
        self.assertEqual(parse(data/invalid.frac), RuntimeError)

    def test_goodInput(self):
        self.assertEqual(parse(data/coral.frac), True)

    def test_defaultFrac(self):
        self.assertEqual(parse(), False)

    def test_FractalFactoryTest(self):
        self.assertEqual(FractalFactory(parse(data/coral.frac)),)

if __name__ == '__main__':
    unittest.main()
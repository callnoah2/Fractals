import unittest
import FractalParser
parse = FractalParser.parse
class TestFractal(unittest.TestCase):
    def test_Phoenix(self):
        """Phoenix fractal configuration and algorithm output the expected colors at key locations"""
        self.assertEqual(getColor(phoenixIter(complex(0, 0), maxIter), 2), '#ffeca5')
        self.assertEqual(getColor(phoenixIter(complex(-0.751, 1.1075), maxIter), 2), '#ffe4b5')
        self.assertEqual(getColor(phoenixIter(complex(-0.2, 1.1075), maxIter), 2), '#ffe5b2')
        self.assertEqual(getColor(phoenixIter(complex(-0.750, 0.1075), maxIter), 2), '#86ff4a')
        self.assertEqual(getColor(phoenixIter(complex(-0.748, -0.1075), maxIter), 2), '#002277')

    def test_Mandelbrot(self):
        """Mandelbrot fractal configuration and algorithm output the expected colors at key locations"""
        # test the pixel color...
        maxIter = 115
        self.assertEqual(Palette.getColor(mBrotIter(complex(0, 0), maxIter), 1), '#7D387D')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.751, 1.1075), maxIter), 1), '#E0DC9C')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.2, 1.1075), maxIter), 1), '#CDDC93')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.75, 0.1075), maxIter), 1), '#79D078')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.748, 0.1075), maxIter), 1), '#59C0BD')
        self.assertEqual(Palette.getColor(mBrotIter(complex(-0.7562500000000001, 0.078125), maxIter), 1), '#6ECB8A')

    def test_SpiderColor(self):
        self.assertEqual(Palette.getColor(spider(complex(0, 0), maxIter), 1), '#7D387D')
        self.assertEqual(Palette.getColor(spider(complex(-0.751, 1.1075), maxIter), 1), '#E0DC9C')
        self.assertEqual(Palette.getColor(spider(complex(-0.2, 1.1075), maxIter), 1), '#CDDC93')
        self.assertEqual(Palette.getColor(spider(complex(-0.75, 0.1075), maxIter), 1), '#79D078')
        self.assertEqual(Palette.getColor(spider(complex(-0.748, 0.1075), maxIter), 1), '#59C0BD')
        self.assertEqual(Palette.getColor(spider(complex(-0.7562500000000001, 0.078125), maxIter), 1), '#6ECB8A')

    def test_Julia(self):
        self.assertEqual(Palette.getColor(Julia(complex(0, 0), maxIter), 1), '#7D387D')
        self.assertEqual(Palette.getColor(Julia(complex(-0.751, 1.1075), maxIter), 1), '#E0DC9C')
        self.assertEqual(Palette.getColor(Julia(complex(-0.2, 1.1075), maxIter), 1), '#CDDC93')
        self.assertEqual(Palette.getColor(Julia(complex(-0.75, 0.1075), maxIter), 1), '#79D078')
        self.assertEqual(Palette.getColor(Julia(complex(-0.748, 0.1075), maxIter), 1), '#59C0BD')
        self.assertEqual(Palette.getColor(Julia(complex(-0.7562500000000001, 0.078125), maxIter), 1), '#6ECB8A')

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
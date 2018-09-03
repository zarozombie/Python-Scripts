import unittest
import mathz

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathz.add(10, 5), 15)
        self.assertEqual(mathz.add(-1, 1), 0)
        self.assertEqual(mathz.add(-1, -1), -2)
        
    def test_subtract(self):
        self.assertEqual(mathz.subtract(10, 5), 5)
        self.assertEqual(mathz.subtract(-1, 1), -2)
        self.assertEqual(mathz.subtract(-1, -1), -0)

    def test_multiply(self):
        self.assertEqual(mathz.multiply(10, 5), 50)
        self.assertEqual(mathz.multiply(-1, 1), -1)
        self.assertEqual(mathz.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(mathz.divide(10, 5), 2)
        self.assertEqual(mathz.divide(-1, 1), -1)
        self.assertEqual(mathz.divide(-1, -1), 1)  

        with self.assertRaises(ValueError):
            mathz.divide(10, 0)  

if __name__ == '__main__':
    unittest.main()
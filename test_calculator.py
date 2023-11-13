import unittest
from calculator import Calculator  # Assuming Calculator is the name of your calculator class or module

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Initialize any resources or configurations needed for each test
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(5, 7)
        self.assertEqual(result, 12)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.multiply(3, 6)
        self.assertEqual(result, 18)

    def test_division(self):
        result = self.calculator.divide(20, 5)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(8, 0)

if __name__ == '__main__':
    unittest.main()

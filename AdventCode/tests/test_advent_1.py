import unittest
from src.AdventCode.advent_code_1 import CalculateTheRequiredFuel


class MyTestCase(unittest.TestCase):
    def test_calculate_fuel_required(self):
        calculating_the_required_fuel = CalculateTheRequiredFuel()
        sample_fuel_to_calculate = 50
        expected_return_value = 14
        actual_return_value = calculating_the_required_fuel.calculate_fuel_required(sample_fuel_to_calculate)
        self.assertEqual(expected_return_value, actual_return_value)


if __name__ == '__main__':
    unittest.main()

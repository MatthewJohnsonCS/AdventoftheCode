import unittest
from unittest.mock import MagicMock

from src.AdventCode.advent_code_2 import CustomComputer


class MyTestCase(unittest.TestCase):
    def test_run_custom_computer(self):
        custom_computer = CustomComputer()
        expected_return_value = [30, 5, 6, 0, 99, 10, 20]
        # custom_computer.turn_opcodes_into_list = MagicMock()
        # custom_computer.turn_opcodes_into_list.return_value = [1, 5, 6, 0, 99, 10, 20]
        actual_return_value = custom_computer.run_through_computer()
        self.assertEqual(expected_return_value, actual_return_value)


if __name__ == '__main__':
    unittest.main()

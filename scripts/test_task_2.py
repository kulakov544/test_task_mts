import unittest
from task_2 import remove_small_number

class TestRemoveSmallNumber(unittest.TestCase):
    def test_example_1(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [2, 3, 4, 5]
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_example_2(self):
        input_list = [5, 3, 2, 1, 4]
        expected_output = [5, 3, 2, 4]
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_example_3(self):
        input_list = [2, 2, 1, 2, 1]
        expected_output = [2, 2, 2, 1]
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_single_element(self):
        input_list = [10]
        expected_output = []
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_multiple_minimum_elements(self):
        input_list = [3, 2, 1, 1, 4]
        expected_output = [3, 2, 1, 4]
        self.assertEqual(remove_small_number(input_list), expected_output)

    def test_all_elements_same(self):
        input_list = [5, 5, 5, 5]
        expected_output = [5, 5, 5]
        self.assertEqual(remove_small_number(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

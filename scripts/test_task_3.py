import unittest
from task_3 import increment_string

class TestIncrementString(unittest.TestCase):
    def test_example_1(self):
        input_str = 'foo'
        expected_output = 'foo1'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_example_2(self):
        input_str = 'foobar23'
        expected_output = 'foobar24'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_example_3(self):
        input_str = 'foo0042'
        expected_output = 'foo0043'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_example_4(self):
        input_str = 'foo9'
        expected_output = 'foo10'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_example_5(self):
        input_str = 'foo099'
        expected_output = 'foo100'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_empty_string(self):
        input_str = ''
        expected_output = '1'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_no_number(self):
        input_str = 'hello'
        expected_output = 'hello1'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_leading_zeros(self):
        input_str = 'prefix000'
        expected_output = 'prefix001'
        self.assertEqual(increment_string(input_str), expected_output)

    def test_number_with_all_nines(self):
        input_str = 'test999'
        expected_output = 'test1000'
        self.assertEqual(increment_string(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()

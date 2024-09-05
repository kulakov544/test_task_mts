import unittest
from task_1 import sort_str

class TestSortStr(unittest.TestCase):
    def test_example_1(self):
        input_str = "is2 Thi1s T4est 3a"
        expected_output = "Thi1s is2 3a T4est"
        self.assertEqual(sort_str(input_str), expected_output)

    def test_example_2(self):
        input_str = "4of Fo1r pe6ople g3ood th5e the2"
        expected_output = "Fo1r the2 g3ood 4of th5e pe6ople"
        self.assertEqual(sort_str(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = ""
        self.assertEqual(sort_str(input_str), expected_output)

    def test_single_word(self):
        input_str = "word1"
        expected_output = "word1"
        self.assertEqual(sort_str(input_str), expected_output)

    def test_words_without_numbers(self):
        input_str = "hello world"
        expected_output = "В слове hello отсутствует число."
        self.assertEqual(sort_str(input_str), expected_output)

    def test_words_with_multiple_numbers(self):
        input_str = "word2 word1 word3"
        expected_output = "word1 word2 word3"
        self.assertEqual(sort_str(input_str), expected_output)

    def test_words_with_same_number(self):
        input_str = "word1 word1 word1"
        expected_output = "word1"
        self.assertEqual(sort_str(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()

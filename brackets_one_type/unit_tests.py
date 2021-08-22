import unittest

from brackets import check_brackets


class TestBrackets(unittest.TestCase):
    def test_simple_cases(self):
        """
        Test for brackets using expeted input values. Inputs have to start with
        a left bracket, each left brackets has to be closed by a right bracket.
        In the end, no bracket can be left unclosed.
        """
        parameters_list = [
            ("(", False),
            (")", False),
            ("()", True),
            (")(", False),
            ("()()", True),
            (")()(", False),
            ("()()(", False),
            ("((((()))))", True),
            ("())", False),
            ("(()", False),
        ]

        for input_string, expected_output in parameters_list:
            with self.subTest():
                self.assertEqual(check_brackets(input_string), expected_output)

    def test_input_sanitization(self):
        """
        Test for non-expected inputs.
        """
        parameters_list = [
            "",
            "(x)",
            "()x",
            "2",
            " ",
            "\\",
            "''",
            "().",
        ]

        for input_string in parameters_list:
            with self.subTest():
                self.assertRaises(ValueError, check_brackets, input_string)


if __name__ == "__main__":
    unittest.main()

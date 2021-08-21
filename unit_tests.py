import unittest

from brackets import check_brackets

# brackets = __import__("brackets.py")
print(check_brackets(""))


# class TestBrackets(unittest.TestCase):
#     def test_simple_cases(self):
#         """
#         Docstring
#         """
#         with self.subTest():
#             self.assertEqual(check_brackets("("), False)
#         with self.subTest():
#             self.assertEqual(check_brackets(")"), False)
#         with self.subTest():
#             self.assertEqual(check_brackets("()"), True)


class TestBrackets(unittest.TestCase):
    def test_simple_cases(self):
        """
        Test for brackets.
        """
        parameters_list = [
            ("", False),
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
            ("(x)", False),
            ("()x", False),
            ("2", False),
            (" ", False),
            ("\\", False),
            ("''", False),
            ("().", False),
        ]

        for input_string, expected_output in parameters_list:
            with self.subTest():
                self.assertEqual(check_brackets(input_string), expected_output)


if __name__ == "__main__":
    unittest.main()

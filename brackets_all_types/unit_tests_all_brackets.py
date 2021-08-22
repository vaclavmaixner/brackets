import unittest

from all_brackets import check_all_bracket_types


class TestBrackets(unittest.TestCase):
    def test_simple_cases(self):
        """
        Test for brackets.
        """
        parameters_list = [
            ("(", False),
            ("[", False),
            ("[]", True),
            ("}{", False),
            ("()()[]{}()", True),
            (")()[]{}()", False),
            ("([)]", False),
            ("{{{()}}", False),
            ("[()]({}){[]}", True),
            ("[()]({}){[]}(", False),
            ("[()]({}){[]})", False),
            ("[({))]", False),
            ("[({)}]", False),
        ]

        for input_string, expected_output in parameters_list:
            with self.subTest():
                self.assertEqual(check_all_bracket_types(input_string), expected_output)

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
                self.assertEqual(check_all_bracket_types(input_string), expected_output)


if __name__ == "__main__":
    unittest.main()

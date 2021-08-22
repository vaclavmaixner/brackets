def contains_nonbracket_characters(input_string):
    for char in input_string:
        if char not in "()":
            return True
    return False


def check_brackets(input_string):
    """Check if a string contains correct brackets.
    If input contains nonbracket characters, raise error.
    Rules:
        A left bracket must be closed by a right bracket.
        A right bracket must close some left bracket.
        In the end, all brackets have to have an appropriate pair of opposite bracket.
    """
    if not contains_nonbracket_characters(input_string) and input_string:
        opened_brackets = 0

        for char in input_string:
            if char == "(":
                opened_brackets += 1
            elif char == ")":
                opened_brackets -= 1

            if opened_brackets < 0:
                return False  # Trying to close without having a left bracket.

        return opened_brackets == 0  # All brackets must be paired at the end.
    else:
        raise ValueError(
            "Unexpected character in input string. Expected characters are '(' and ')'."
        )

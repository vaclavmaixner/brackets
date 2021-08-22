def check_all_bracket_types(input_string):
    """
    Check if a input string contains correct bracket notation. Returns false
    if nonbracket characters are introduced.
    Rules:
        Each left bracket must be closed by an appropriate right bracket.
        Each right bracket must be able to close an appropriate left bracket.
    """

    brackets_mapper = {")": "(", "]": "[", "}": "{"}
    left_brackets = list(brackets_mapper.values())
    right_brackets = list(brackets_mapper.keys())

    magazine = []  # Keep track of the last opened bracket.
    for char in input_string:
        if char in left_brackets:
            magazine.append(char)  # Opening new brackets is always possible.
        elif char in right_brackets and magazine:
            if magazine[-1] == brackets_mapper[char]:
                magazine.pop()  # Close the last left bracket.
            else:
                return False  # Wrong type of closing bracket.
        else:
            return False  # Started with a right bracket or unexpected input.

    if not magazine:
        return True
    else:
        return False

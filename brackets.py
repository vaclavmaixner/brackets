input_string = "("
input_examples = [
    "",
    "(",
    ")",
    "()",
    ")(",
    "))",
    "((",
    "(()",
    "(()())",
    "((())())",
    "(()))",
    "gg",
]


def contains_nonbracket_characters(input_string):
    for char in input_string:
        if char not in "()":
            return True
    return False


def check_brackets(input_string):
    """Check if a string contains correct brackets.
    Things to keep in mind: non bracket only input
    Rules:
                    every opened left bracket has to be closed by a right bracket eventually
                    right bracket cannot come before a left bracket

    """
    if not contains_nonbracket_characters(input_string) and input_string:
        opened_brackets = 0
        is_correct = False

        for char in input_string:
            if char == "(":
                opened_brackets += 1
            elif char == ")":
                opened_brackets -= 1
            else:
                raise Exception("Bad characters.")
                # raise ValueError('Input string contains unexpected cahracters. Expected characters are ( and ).')

            if opened_brackets < 0:
                return False
                # raise ValueError('Tried to close a non-existent bracket.')

        # print(opened_brackets==0)f d

        return opened_brackets == 0
    else:
        return False


def check_brackets_list(list_input_string):
    for input_string in list_input_string:
        print(input_string, check_brackets(input_string))


# check_brackets_list(input_examples)

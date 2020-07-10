
def bool_input(prompt: str) -> bool:
    """Prompt user for yes/no boolean input.

    Returns True if user response is 'y'/'Y'/'yes'/'YES'. Otherwise, False.

    Args:
        prompt (str): Prompt to display.

    Returns:
        bool: User boolean response.
    """
    response = input(f'{prompt} (y/N) ')
    return response.lower() in ['y', 'yes']


def int_input(prompt: str, input_range: int) -> int:
    """Prompt user for an integer value.

    Args:
        prompt (str): Prompt to display.
        input_range (int): Acceptable range of integers.

    Raises:
        ValueError: Reprompt on invalid user input.

    Returns:
        int: Validated user integer response.
    """
    response = -1
    valid = False
    while not valid:
        try:
            response = int(input(f'{prompt} (0-{input_range - 1}): '))
            if response in range(input_range):
                valid = True
            else:
                raise ValueError(f'{response} is not in range ' +
                                 f'0-{input_range - 1}.')
        except ValueError:
            print(f'\tInvalid input. Enter an integer from ' +
                  f'0-{input_range - 1}.')

    return response


def str_input(prompt: str) -> str:
    """Prompt user for string value.

    Args:
        prompt (str): Prompt to display.

    Returns:
        str: User string response.
    """
    return input(f'{prompt} ')

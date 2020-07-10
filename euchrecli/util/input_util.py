
def bool_input(prompt: str) -> bool:
    response = input(f'{prompt} (y/N) ')
    return response.lower() in ['y', 'yes']


def int_input(prompt: str, input_range: int) -> int:
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
    return input(f'{prompt} ')

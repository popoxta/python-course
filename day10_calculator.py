from utils.input import get_numeric_input
from utils.prompt import prompt

operations = {
    'multiply': lambda a, b: a * b,
    'add': lambda a, b: a + b,
    'subtract': lambda a, b: a - b,
    'divide': lambda a, b: a / b
}


def get_operation_input():
    return prompt(name='operation', message='Select an operation', choices=list(operations.keys()))


def get_continue_operation(num):
    return prompt(name='continue', message=f'Continue operation with {num}?', choices=['yes', 'no']) == 'yes'


def get_number(is_first):
    return get_numeric_input(f'What is the {'first' if is_first else 'next'} number?\n')


def calculate(first_number, second_number, operation):
    return operations[operation](first_number, second_number)


def run_calculator(first_number=None):
    first_number = first_number if first_number else get_number(True)
    operation = get_operation_input()
    second_number = get_number(False)

    result = calculate(first_number, second_number, operation)
    print(f'The result of the operation is {result}')

    if get_continue_operation(result):
        run_calculator(result)
    else:
        print('Goodbye')
        return


def main():
    run_calculator()


if __name__ == '__main__':
    main()

def get_text_input(message):
    user_input = input(message if message else 'Enter text')
    if not user_input.isalpha():
        print('Please enter text only!')
        return get_text_input(message)
    else:
        return user_input


def get_numeric_input(message):
    user_input = input(message if message else 'Enter a number')
    if not user_input.isnumeric():
        print('Please enter numbers only!')
        return get_numeric_input(message)
    else:
        return int(user_input)

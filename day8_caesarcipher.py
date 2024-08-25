from utils.prompt import prompt

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

ALPHABET_LENGTH = len(ALPHABET)


def cipher(message, shift, shift_forwards):
    return [ALPHABET[(ALPHABET.index(val) + shift if shift_forwards else ALPHABET.index(val) - shift) % ALPHABET_LENGTH]
            for val in message.lower()]


def get_text_input():
    user_input = input('What is the word that must be shifted?')
    if not user_input.isalpha():
        print('Please enter text only!')
        return get_text_input()
    else:
        return user_input


def get_numeric_input():
    user_input = input('What is your shift value?')
    if not user_input.isnumeric():
        print('Please enter numbers only!')
        return get_numeric_input()
    else:
        return int(user_input)


def cipher_input():
    text = get_text_input().lower()
    shift_value = get_numeric_input()
    is_forwards = prompt(name='is_forward', message='Forwards or backwards?',
                         choices=['forwards', 'backwards']) == 'forwards'
    ciphered_text = ''.join(cipher(message=text, shift=shift_value, shift_forwards=is_forwards))
    print(f'Your ciphered text is {ciphered_text}')
    if prompt(name='again', message='Again?', choices=['yes', 'no']) == 'yes':
        cipher_input()
    else:
        print('BYE BITCH')


def main():
    cipher_input()


main()

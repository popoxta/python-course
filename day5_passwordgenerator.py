import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def get_random_values(num_letters, num_numbers, num_symbols):
    values = [{"selection": LETTERS, "num": num_letters},
              {"selection": NUMBERS, "num": num_numbers},
              {"selection": SYMBOLS, "num": num_symbols}]

    final = []

    for value in values:
        for i in range(value['num']):
            final.extend(random.choice(value['selection']))

    return final


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = get_random_values(nr_letters, nr_numbers, nr_symbols)
    print(f'Your password is ${''.join(password)} !!!')

    scramble_password = input(f"Would you like to scramble it? y/n\n")
    if not scramble_password:
        print('Goodbye!')
        return

    scrambled_password = random.sample(password, len(password))
    print(f'Your scrambled password is ${''.join(scrambled_password)} !!!')
    print('Goodbye!')


main()

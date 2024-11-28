# Number Guessing Game
import random

from utils.input import get_numeric_input
from utils.prompt import prompt

MAX_NUMBER = 100
MIN_NUMBER = 1
DIFFICULTIES = {
    'easy': {
        'tries': 10
    },
    'hard': {
        'tries': 5
    }
}


def get_random_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def select_difficulty():
    return DIFFICULTIES[prompt(name='difficulty', message='Pick a difficulty', choices=DIFFICULTIES.keys())]


def get_user_guess():
    return get_numeric_input(message='Make a guess: ')


def check_continue_playing():
    return prompt(name='continue', message='Play again?', choices=['yes', 'no']) == 'yes'


def play_number_guessing_game():
    print(f'I\'m thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}!\n')

    random_number = get_random_number()
    tries_left = select_difficulty()['tries']

    while tries_left:
        guess = get_user_guess()
        if guess == random_number:
            print(f'You got it! The number was {random_number}\n')
            return
        else:
            print('Too high!' if guess > random_number else 'Too low!')
            tries_left -= 1
            print(f'You have {tries_left} guesses remaining...\n')

    print(f'Uh oh - you ran out of guesses! The random number was {random_number}! Too bad...')


def main():
    print('Welcome to the Number Guessing Game! (NGG)')
    play_number_guessing_game()

    while check_continue_playing():
        play_number_guessing_game()

    print('Goodbye!')


if __name__ == '__main__':
    main()

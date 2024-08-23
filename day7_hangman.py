from random_word import RandomWords
from resources.hangman import stages
from utils.prompt import prompt


def play_game():
    tries_left = 6
    random_word = RandomWords().get_random_word().lower()
    print(random_word)
    guessed_word = ['_'] * len(random_word)
    guessed_letters = []

    print('Welcome to HANGMAN!\n')
    print_hangman_stage(tries_left)
    print(f'{''.join(guessed_word)}\n')

    while tries_left > 0:
        player_input = get_player_input()

        if player_input in guessed_letters:
            print("Letter has already been guessed!")
            continue

        if player_input in random_word:
            print(f"\nYou guessed right! '{player_input}' is in the secret word.")
            guessed_letters.append(player_input)
            letter_indexes = [i for i, v in enumerate(random_word) if v == player_input]
            for i in letter_indexes:
                guessed_word[i] = player_input
        else:
            print(f"\nUh oh! '{player_input}' is not in the secret word.")
            tries_left -= 1

        joined_guessed_word = ''.join(guessed_word)
        print_hangman_stage(tries_left)
        print(joined_guessed_word)

        if joined_guessed_word == random_word:
            print(f'Congratulations! You saved the lad! The word was {random_word}!\n')
            break

    if tries_left == 0:
        print(f'Unfortunately dear Jeremy has been killed for your mistakes. The secret word was {random_word}!\n')


def get_player_input():
    player_input = input('Guess a letter:\n')

    if not (player_input.isalpha() and len(player_input) == 1):
        print('Please enter a single letter!\n')
        return get_player_input()
    return player_input.lower()


def print_hangman_stage(stage_number):
    print(stages[stage_number])


def main():
    play_game()
    if prompt(name='restart', message='Restart?', choices=['Yes', 'No']) == 'Yes':
        play_game()
    else:
        print('Goodbye!')
        return


main()

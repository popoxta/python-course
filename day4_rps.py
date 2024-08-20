import random
from utils.prompt import prompt

OPPONENT_NAME = 'COMPUTER'
CHOICES = ['rock', 'paper', 'scissors']


def get_random_choice():
    return random.choice(CHOICES)


def get_user_choice():
    return prompt(message='Rock, paper or scissors?', choices=CHOICES, name='player_choice')


def is_player_win(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'

    if ((player_choice == 'rock' and computer_choice == 'scissors')
            or (player_choice == 'scissors' and computer_choice == 'paper')
            or (player_choice == 'paper' and computer_choice == 'rock')):
        return 'pwin'

    return 'cwin'


def play_round():
    player_choice = get_user_choice()
    computer_choice = get_random_choice()

    print(f'{OPPONENT_NAME} chose {computer_choice}!')
    return is_player_win(player_choice, computer_choice)


def play_game(player_name):
    computer_score = 0
    player_score = 0

    print(f'\nWelcome to ROCK PAPER SCISSORS {player_name}!\nYour opponent is {OPPONENT_NAME}.')
    print('The game starts now!\n')

    while player_score < 3 and computer_score < 3:
        round_result = play_round()

        match round_result:
            case 'pwin':
                print(f'Congrats, {player_name} won!\n')
                player_score += 1
            case 'cwin':
                print(f'{OPPONENT_NAME} won!\n')
                computer_score += 1
            case _:
                print('It\'s a draw!\n')

        print(f'COMPUTER: {computer_score}, PLAYER: {player_score}')

    winner = player_name if player_score > computer_score else OPPONENT_NAME
    print('\nTHE GAME IS NOW OFFICIALLY OVER!')
    print(f'The winner is...\n{winner}!!!!\n')

    if prompt(name='play_again', message='Play again?', choices=['yes', 'no']) == 'yes':
        play_game(player_name)

    print(f'Goodbye {player_name}!')
    return


def main():
    player_name = input('What is your name?\n')
    play_game(player_name)


main()

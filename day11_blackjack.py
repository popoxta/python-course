import random
from typing import List, NewType

from utils.prompt import prompt

Cards = NewType('Cards', List[int | str])

BASE_DECK = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
SPECIAL_CARDS_VALUE = 10
PLAYER_NAME = 'player'
COMPUTER_NAME = 'computer'


def check_is_blackjack(score: int):
    return score == 0


def deal_cards(num_cards: int) -> Cards:
    """Deals n number of cards randomly chosen from the deck"""
    return random.choices(population=BASE_DECK, k=num_cards)


def add_cards_to_hand(cards: Cards, hand: Cards):
    """Returns the modified hand with new card/s added"""
    return Cards(cards + hand)


def calculate_hand(cards: Cards):
    """Calculates the score of the given hand"""
    numeric_cards = [x for x in cards if isinstance(x, int)]
    special_cards = [SPECIAL_CARDS_VALUE for x in cards if isinstance(x, str) and x != 'ace']
    aces = [x for x in cards if x == 'ace']

    if len(aces) == 1 and len(numeric_cards) == 1 and numeric_cards[0] == 10:
        return 0

    score = sum(numeric_cards + special_cards)

    for _ in aces:
        score += (11 if score < 10 else 1)

    return score


def print_round_details(cards: Cards, owner: str, score: int):
    """Prints the round details for the given cards, score and owner"""
    print(f'The {owner}\'s cards are: {cards}')
    print(f'{owner}\'s score: {score}\n')


def get_cards_result(cards: Cards) -> dict:
    """Retrieves the results including score the score, and win, lose and blackjack indicators"""
    score = calculate_hand(cards)
    results = {
        'score': score,
        'win': False,
        'lose': False,
        'blackjack': check_is_blackjack(score)
    }

    if results['blackjack'] or score == 21:
        results['win'] = True

    elif score > 21:
        results['lose'] = True

    return results


def check_game_over(results, name: str) -> bool:
    """Checks if a game is over based on the given results"""
    is_blackjack = results['blackjack']
    is_win = is_blackjack or results['win']
    is_lose = results['lose']

    if is_win:
        print(f'{name} WINS!!! It is {'' if is_blackjack else 'not'} a blackjack!!!')
    elif is_lose:
        print(f'{name} LOSES!!! It is {'' if is_blackjack else 'not'} a blackjack!!!')

    return is_win or is_lose


def check_player_continue_drawing():
    """Prompts the player if they would like to continue drawing cards"""
    return (prompt(name='continue', message='Draw a card?', choices=['yes', 'no'])) == 'yes'


def check_play_again():
    """Prompts the player if they would like to play another game"""
    return (prompt(name='continue', message='\nPlay again?', choices=['yes', 'no'])) == 'yes'


def play_round(cards: Cards, is_player_turn: bool, name: str):
    """Plays a round of blackjack for the player or computer npc"""
    print(f'{name}\'s turn!')
    results = get_cards_result(cards)

    while check_player_continue_drawing() if is_player_turn else get_cards_result(cards)['score'] <= 17:
        print(f'{name} pulled a card!')
        cards = add_cards_to_hand(cards, deal_cards(1))
        results = get_cards_result(cards)
        print_round_details(cards, owner=name if is_player_turn else 'computer', score=results['score'])
        if results['lose'] or results['win']:
            break
    print(f'{name}\'s turn is complete!')
    return results, cards


def play_game():
    """Plays a full game of blackjack"""

    def check_player_results(results):
        return check_game_over(results, PLAYER_NAME)

    def check_computer_results(results):
        return check_game_over(results, COMPUTER_NAME)

    def check_end_game(player_round_results, computer_round_results):
        return check_player_results(player_round_results) or check_computer_results(computer_round_results)

    print('Welcome to BLACKOJACKO!!!\n')

    # setup cards
    player_cards = deal_cards(2)
    computer_cards = deal_cards(1)

    player_results = get_cards_result(player_cards)
    computer_results = get_cards_result(computer_cards)

    print_round_details(cards=player_cards, owner=PLAYER_NAME, score=player_results['score'])
    print_round_details(cards=computer_cards, owner=COMPUTER_NAME, score=computer_results['score'])

    is_game_over = check_end_game(player_results, computer_results)

    while not is_game_over:
        player_results, player_cards = play_round(player_cards, True, PLAYER_NAME)
        if check_end_game(player_results, computer_results):
            return

        computer_results, computer_cards = play_round(computer_cards, False, COMPUTER_NAME)
        is_game_over = check_end_game(player_results, computer_results)


def main():
    play_game()
    while check_play_again():
        play_game()


if __name__ == '__main__':
    main()

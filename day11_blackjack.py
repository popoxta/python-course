import random
from typing import List, NewType

Cards = NewType('Cards', List[int | str])

BASE_DECK = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
SPECIAL_CARDS_VALUE = 10


def check_is_blackjack(score: int):
    return score == 21


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
        score += (11 if score < 21 else 1)

    return score


def print_round_details(cards: Cards, owner: str):
    print(f'The {owner}\'s cards are: {cards}')
    print(f'{owner}\'s score: {calculate_hand(cards)}\n')


def check_if_win(cards: Cards):
    score = calculate_hand(cards)
    if score == 0 or score == 21:
        return {
            'score': score,
        }


def play_game():
    print('Welcome to BLACKOJACKO!!!')

    # setup cards
    player_cards = deal_cards(2)
    computer_cards = deal_cards(1)
    print_round_details(player_cards, 'Player')
    print_round_details(computer_cards, 'Computer')



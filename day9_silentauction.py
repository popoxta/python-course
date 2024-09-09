from utils.input import get_text_input, get_numeric_input
from utils.prompt import prompt


def get_bidder_name_and_bid(nth_bidder):
    name = get_text_input(f'Enter a name for bidder no.{nth_bidder}:\n')
    bid = get_numeric_input(f'Enter a bid for {name}:\n')
    return name, bid


def check_continue_to_next_bidder():
    return prompt(name='continue', message='\nAdd another bidder?', choices=['Yes', 'No']) == 'Yes'


def find_highest_bid(bids):
    return max(zip(bids.values(), bids.keys()))[1]


def run_silent_auction():
    is_over = False
    bids = {}

    while not is_over:
        name, bid = get_bidder_name_and_bid(len(bids.keys()) + 1)
        bids[name] = bid
        is_over = not check_continue_to_next_bidder()

    highest_bidder = find_highest_bid(bids)
    print(f'The highest bidder is {highest_bidder} with a bid of {bids[highest_bidder]}!!!\n')


def main():
    print('Welcome to the SILENT AUCTION!!!\n')
    run_silent_auction()


main()

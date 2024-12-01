# Coffee Machine
#
# Starting resources
#   300ml water
#   200ml milk
#   100g coffee
#
# Coins
#    Penny (1 cent)
#    Nickel (5 cent)
#   Dime (10 cent)
#   Quarter (25 cent)
#
# Coffee Types:
#
# Espresso
#   50ml water
#   18g coffee
#   $1.50
#
# Latte
#   200ml water
#   18g coffee
#   150ml milk
#   $2.50
#
# Cappuccino
#   250ml water
#   24g coffee
#   100ml milk
#   $3.50
#
# Program Requirements
#   Print a report (status - coins, resources) on 'report' prompt
#   Turn off machine with 'off' prompt
#   Check resources sufficient for order
#   If insufficient resources or money, return money to user
#   Input money (penny, nickel, dime, quarters...)
#   Calculate change based on cost of drink
#   Deduct resources when making drink
from typing import TypedDict, List
from utils.input import get_numeric_input
from utils.prompt import prompt


class Resources(TypedDict):
    water: int
    milk: int
    coffee: int


class CoffeeMachine(TypedDict):
    balance: int
    resources: Resources


COIN_VALUES = {
    'penny': 1,
    'nickel': 5,
    'dime': 10,
    'quarter': 25
}

COFFEE_TYPES = {
    'espresso': {
        'resources': {
            'water': 50,
            'coffee': 18,
            'milk': 0
        },
        'cost': 150
    },
    'latte': {
        'resources': {
            'water': 200,
            'coffee': 18,
            'milk': 150
        },
        'cost': 250
    },
    'cappuccino': {
        'resources': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'cost': 350
    }
}


def convert_cents_to_dollars(money: int | float, reverse: bool = False):
    return int(100 * money) if reverse else money / 100


def get_new_machine() -> CoffeeMachine:
    return {
        'balance': 0,
        'resources': {
            'milk': 200,
            'water': 300,
            'coffee': 100
        },
    }


def print_report(machine: CoffeeMachine):
    print(f'Balance: ${convert_cents_to_dollars(machine['balance'])}')
    resources = machine['resources']
    for key, value in resources.items():
        print(f'{key.title()}: {value}ml')


def get_machine_input():
    return prompt(name='input', message='Choose a menu option',
                  choices=[x.title() for x in COFFEE_TYPES.keys()] + ['Turn Off Machine', 'Print Resources'])


def process_coin_input(item_cost: int):
    coin_input = {e: get_numeric_input(f'How many {e}s?\n') * COIN_VALUES[e] for e in COIN_VALUES.keys()}
    total_coin_value = sum(coin_input.values())

    difference_between_cost_and_input = item_cost - total_coin_value
    is_input_sufficient = difference_between_cost_and_input < 0

    if difference_between_cost_and_input > 0:
        print(f'Not enough money! You are short ${convert_cents_to_dollars(item_cost - total_coin_value)}!')
        print(f'Returning ${convert_cents_to_dollars(total_coin_value)}...')
        total_coin_value = 0
    elif is_input_sufficient:
        print(f'You paid too much, returning ${convert_cents_to_dollars(abs(difference_between_cost_and_input))}...')
        total_coin_value = item_cost
    return {
        'is_transaction_success': is_input_sufficient,
        'balance': total_coin_value
    }


def update_machine_balance(machine: CoffeeMachine, balance_addition: int):
    machine['balance'] += balance_addition
    return machine


def get_order_item_details(order_item: str):
    return COFFEE_TYPES[order_item]


def get_order_resources(order_item: str) -> Resources:
    return get_order_item_details(order_item)['resources']


def check_resources_sufficient(resources_required: Resources, machine: CoffeeMachine):
    for key, value in resources_required.items():
        machine_balance = machine['resources'][key]  # type: ignore
        if not machine_balance >= value:
            print(f'Not enough {key} in the machine! Requires {value}, has {machine_balance}...')
            return False
    return True


def update_machine_resources(resources_removed: Resources, machine: CoffeeMachine):
    for key, value in resources_removed:
        machine['resources'][key] -= value  # type: ignore
    return machine

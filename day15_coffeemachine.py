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
from typing import TypedDict


class MachineResources(TypedDict):
    water: int
    milk: int
    coffee: int


class CoffeeMachine(TypedDict):
    balance: int
    resources: MachineResources


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


print_report(get_new_machine())

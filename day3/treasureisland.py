import inquirer


def prompt(name, message, choices):
    response = inquirer.prompt([inquirer.List(name, message, choices)])
    return response[name]


def main():
    print('Welcome to the Linwood hood!\n')
    print('Your mission is to survive.\n')

    print('You find yourself in a dark alleyway, you can hear faint shouting and yelling in the background.')
    direction = prompt('direction', 'Do you turn left or right?', ['left', 'right'])
    if direction == 'right':
        print(f'As you turn {direction}, you immediately run into a bloke reminiscent of a Thwomp. He looks at you, '
              f'and utters a single sentence.\n"You right mate?"\nYou can hardly blink before he shoves a BP pie into '
              f'your face, suffocating and burning you from the inside out.')
        print('\n-- GAME OVER --')
        return
    print(f'You turn ${direction}, running as fast as you can from the sound of Linwood domestics. '
          f'After what feels like an eternity, you realize the scenery has changed and you are no longer stuck'
          f' like a used condom within the alleys of the street.')

    swim_or_wait = prompt('swim_or_wait', 'Swim or wait', ['swim', 'wait'])
    if swim_or_wait == 'swim':
        print('\n-- GAME OVER --')
        return

    door_decision = prompt('door', 'Which door', ['red', 'blue', 'yellow'])
    if door_decision == 'red' or door_decision == 'blue':
        print('\n-- GAME OVER --')
        return
    print('ya did it')


main()

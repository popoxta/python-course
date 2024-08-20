import inquirer

TIP_QUESTIONS = [
    inquirer.List(
        'tip_percent',
        message='How bad do you feel for the waiter?',
        choices=[5, 10, 15, 25, 100]
    )
]


def get_number(message):
    number = input(f'{message}\n')
    if not number.isnumeric():
        print('Fool. That is no number. Try again')
        return get_number(message)
    return int(number)


def main():
    print('Welcome to the tippy!')
    total_bill = get_number('What was the damage today?')
    tip_percent = inquirer.prompt(TIP_QUESTIONS)['tip_percent']
    total_party = get_number('How many fools make up your party?')
    total_cost_per_person = (total_bill + tip_percent / total_bill * 100) / total_party
    print('Each of your party members must cough up ${:0.2f}'.format(total_cost_per_person))


main()

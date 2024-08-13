import inquirer


def prompt(name, message, choices):
    response = inquirer.prompt([inquirer.List(name, message, choices)])
    return response[name]

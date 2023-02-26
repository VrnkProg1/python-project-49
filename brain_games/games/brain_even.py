from random import randint


def RULES_OF_THE_GAME():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rules


def the_number_to_check():
    number = randint(1, 100)
    return number


def parity_check():
    number = the_number_to_check()
    if number % 2 == 0:
        correct = 'yes'
    elif number % 2 != 0:
        correct = 'no'
    return correct, number


def logic_of_the_game():
    parity_check()
    correct, number = parity_check()
    return correct, number

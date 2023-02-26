import random


def RULES_OF_THE_GAME():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return rules


def number_for_cheking():
    number = random.randint(0, 5)
    return number


def checking_for_simplicity():
    number = number_for_cheking()
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                correct = 'no'
                break
        else:
            correct = 'yes'
    else:
        correct = 'no'
    return correct, number


def logic_of_the_game():
    checking_for_simplicity()
    correct, number = checking_for_simplicity()
    return correct, number

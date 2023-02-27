from random import randint


RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False


def generate_question_and_answer():
    number = randint(1, 100)
    if parity_check(number):
        correct = 'yes'
    else:
        correct = 'no'
    return correct, number

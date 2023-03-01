from random import randint


RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_parity_check(number):
    if number % 2:
        return False
    else:
        return True


def generate_question_and_answer():
    number = randint(1, 100)
    if is_parity_check(number):
        correct = 'yes'
    else:
        correct = 'no'
    return correct, number

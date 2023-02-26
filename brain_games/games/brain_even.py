from random import randint


RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    if number % 2 == 0:
        correct = 'yes'
    elif number % 2 != 0:
        correct = 'no'
    return correct, number


def generate_question_and_answer():
    number = randint(1, 100)
    correct, number = parity_check(number)
    return correct, number

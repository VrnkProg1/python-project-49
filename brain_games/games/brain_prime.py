import random


RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_check_for_simplicity(number):
    if number <= 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(0, 100)
    if is_check_for_simplicity(number):
        correct = 'yes'
    else:
        correct = 'no'
    return correct, number

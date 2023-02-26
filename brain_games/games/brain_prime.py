import random


RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def checking_for_simplicity(number):
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


def generate_question_and_answer():
    number = random.randint(0, 100)
    correct, number = checking_for_simplicity(number)
    return correct, number

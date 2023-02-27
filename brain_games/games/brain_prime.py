import random


RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def checking_for_simplicity(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False


def generate_question_and_answer():
    number = random.randint(0, 100)
    if checking_for_simplicity(number):
        correct = 'yes'
    else:
        correct = 'no'
    return correct, number

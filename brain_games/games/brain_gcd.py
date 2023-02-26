from random import randint
from math import gcd


RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    correct_value = gcd(first_number, second_number)
    expression = f'{first_number} {second_number}'
    return str(correct_value), expression

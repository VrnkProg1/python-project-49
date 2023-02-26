from random import randint
from math import gcd


def RULES_OF_THE_GAME():
    rules = 'Find the greatest common divisor of given numbers.'
    return rules


def logic_of_the_game():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    correct_value = gcd(first_number, second_number)
    expression = f'{first_number} {second_number}'
    return str(correct_value), expression

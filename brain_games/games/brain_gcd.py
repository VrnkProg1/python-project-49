from random import randint


def rules():
    rules = 'Find the greatest common divisor of given numbers.'
    return rules


def gcd():
    first_number = randint(1, 50)
    second_number = randint(1, 50)
    question = 'Question:'
    expression = f'{first_number} {second_number}'
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    correct_number = first_number + second_number
    correct = str(correct_number)
    return correct, question, expression

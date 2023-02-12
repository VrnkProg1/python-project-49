from random import randint


def rules():
    print('Find the greatest common divisor of given numbers.')


def gcd():
    a = randint(1, 50)
    b = randint(1, 50)
    question = 'Question:'
    expression = f'{a} {b}'
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    correct = a + b
    return correct, question, expression

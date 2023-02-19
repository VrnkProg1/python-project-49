from random import randint


def rules():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rules


def even():
    number = randint(1, 100)
    question = 'Question:'
    if number % 2 == 0:
        correct = 'yes'
    elif number % 2 != 0:
        correct = 'no'
    return correct, question, number

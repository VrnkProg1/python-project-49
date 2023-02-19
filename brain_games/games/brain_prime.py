import random


def rules():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return rules


def prime():
    number = random.randint(2, 100)
    question = 'Question:'
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if (k <= 0):
        correct = 'yes'
    else:
        correct = 'no'
    return correct, question, number

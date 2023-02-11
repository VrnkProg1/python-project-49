import random


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    number = random.randint(2, 100)
    question = 'Question:'
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if (k <= 0):
        correct = 'True'
    else:
        correct = 'False'
    return correct, question, number

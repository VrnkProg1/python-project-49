import random


def rules():
    print('What number is missing in the progression?')


def progression():
    question = 'Question:'
    list = []
    step = random.randint(1, 20)
    first = 1
    while len(list) < 10:
        list.append(first)
        first += step
    index = random.randint(0, 9)
    correct = list[index]
    b = ".."
    list[index] = b
    a = ''
    for i in list:
        a += f'{i} '
    return correct, question, list

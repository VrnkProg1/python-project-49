import random


def rules():
    rules = 'What number is missing in the progression?'
    return rules


def progression():
    question = 'Question:'
    list = []
    step = random.randint(1, 20)
    first = 1
    while len(list) < 10:
        list.append(first)
        first += step
    index = random.randint(0, 9)
    correct_number = list[index]
    missing_number = ".."
    list[index] = missing_number
    progression = ''
    for i in list:
        progression += f'{i} '
    correct = str(correct_number)
    return correct, question, progression

import random


def rules():
    print('What number is missing in the progression?')


def progression():
    list = []
    step = random.randint(1, 20)
    first = random.randint(0, 1000)
    while len(list) < 10:
        list.append(first)
        first += step
    index = random.randint(0, 9)
    val = list[index]
    b = ".."
    list[index] = b
    a = ''
    for i in list:
        a += f'{i} '
    print('Question:', a)
    return val

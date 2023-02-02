import random


def rules():
    print('What is the result of the expression?')


def calc():
    list = ['+', '-', '*']
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.sample(list, 1)
    if operator == ['+']:
        val = value1 + value2
        question = f'{value1} {"+"} {value2}'
    elif operator == ['-']:
        val = value1 - value2
        question = f'{value1} {"-"} {value2}'
    else:
        val = value1 * value2
        question = f'{value1} {"*"} {value2}'
    print('Question: ', question)
    return val

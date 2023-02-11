import random


def rules():
    print('What is the result of the expression?')


def check():
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    operator = random.sample(list_of_operands, 1)
    if operator == ['+']:
        expected_answer = value1 + value2
        expression = f'{value1} {"+"} {value2}'
    elif operator == ['-']:
        expected_answer = value1 - value2
        expression = f'{value1} {"-"} {value2}'
    else:
        expected_answer = value1 * value2
        expression = f'{value1} {"*"} {value2}'
    question = 'Question:'
    return expected_answer, question, expression


def calc():
    check()
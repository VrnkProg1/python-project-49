import random


def rules():
    print('What is the result of the expression?')


def calc():
    question = 'Question:'
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 15)
    value2 = random.randint(1, 15)
    operator = random.sample(list_of_operands, 1)
    if operator == ['+']:
        correct = value1 + value2
        expression = f'{value1} + {value2}'
    elif operator == ['-']:
        correct = value1 - value2
        expression = f'{value1} - {value2}'
    elif operator == ['*']:
        correct = value1 * value2
        expression = f'{value1} * {value2}'
    return correct, question, expression

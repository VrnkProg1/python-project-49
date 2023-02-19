import random


def rules():
    rules = 'What is the result of the expression?'
    return rules


def calc():
    question = 'Question:'
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 15)
    value2 = random.randint(1, 15)
    operator = random.sample(list_of_operands, 1)
    if operator == ['+']:
        correct_number = value1 + value2
        expression = f'{value1} + {value2}'
    elif operator == ['-']:
        correct_number = value1 - value2
        expression = f'{value1} - {value2}'
    elif operator == ['*']:
        correct_number = value1 * value2
        expression = f'{value1} * {value2}'
    correct = str(correct_number)
    return correct, question, expression

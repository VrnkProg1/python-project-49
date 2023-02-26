import random


RULES_OF_GAME = 'What is the result of the expression?'


def generate_expression(value1, value2, operator):
    if operator == ['+']:
        correct_value = value1 + value2
        expression = f'{value1} + {value2}'
    elif operator == ['-']:
        correct_value = value1 - value2
        expression = f'{value1} - {value2}'
    elif operator == ['*']:
        correct_value = value1 * value2
        expression = f'{value1} * {value2}'
    return correct_value, expression


def generate_question_and_answer():
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 15)
    value2 = random.randint(1, 15)
    operator = random.sample(list_of_operands, 1)
    correct_value, expression = generate_expression(value1, value2, operator)
    return str(correct_value), expression

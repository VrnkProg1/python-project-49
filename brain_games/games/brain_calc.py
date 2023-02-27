import random


RULES_OF_GAME = 'What is the result of the expression?'


def calculate_value(value1, value2, operator):
    if operator == '+':
        correct_value = value1 + value2
    elif operator == '-':
        correct_value = value1 - value2
    elif operator == '*':
        correct_value = value1 * value2
    return correct_value


def generate_question_and_answer():
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 15)
    value2 = random.randint(1, 15)
    operator = random.choice(list_of_operands)
    correct_value = calculate_value(value1, value2, operator)
    expression = f'{value1} {operator} {value2}'
    return str(correct_value), expression

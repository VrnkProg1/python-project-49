import random


def RULES_OF_THE_GAME():
    rules = 'What is the result of the expression?'
    return rules


def numbers_and_operators():
    list_of_operands = ['+', '-', '*']
    value1 = random.randint(1, 15)
    value2 = random.randint(1, 15)
    operator = random.sample(list_of_operands, 1)
    return value1, value2, operator


def calculation_of_the_expression():
    value1, value2, operator = numbers_and_operators()
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


def logic_of_the_game():
    calculation_of_the_expression()
    correct_value, expression = calculation_of_the_expression()
    return str(correct_value), expression

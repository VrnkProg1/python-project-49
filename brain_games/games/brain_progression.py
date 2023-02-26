import random


def RULES_OF_THE_GAME():
    rules = 'What number is missing in the progression?'
    return rules


def first_element_and_step():
    step = random.randint(1, 20)
    first_element = random.randint(1, 20)
    return step, first_element


def generating_a_progression():
    step, first_element = first_element_and_step()
    list = []
    while len(list) < 10:
        list.append(first_element)
        first_element += step
    index = random.randint(0, 9)
    correct_value = list[index]
    missing_number = ".."
    list[index] = missing_number
    progression = ''
    for i in list:
        progression += f'{i} '
    return correct_value, progression


def logic_of_the_game():
    correct_value, progression = generating_a_progression()
    return str(correct_value), progression

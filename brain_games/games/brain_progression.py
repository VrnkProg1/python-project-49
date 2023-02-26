import random


RULES_OF_GAME = 'What number is missing in the progression?'


def generating_progression(step, first_element):
    progression = []
    while len(progression) < 10:
        progression.append(first_element)
        first_element += step
    return progression


def generate_question_and_answer():
    step = random.randint(1, 20)
    first_element = random.randint(1, 20)
    progression = generating_progression(step, first_element)
    index = random.randint(0, 9)
    correct_value = progression[index]
    missing_number = ".."
    progression[index] = missing_number
    clean_progression = ''
    for i in progression:
        clean_progression += f'{i} '
    return str(correct_value), clean_progression

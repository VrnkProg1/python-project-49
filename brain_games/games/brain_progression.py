import random


RULES_OF_GAME = 'What number is missing in the progression?'


def generate_progression(step, first_element, lenght):
    progression = []
    while len(progression) < lenght:
        progression.append(first_element)
        first_element += step
    return progression


def generate_question_and_answer():
    lenght = random.randint(5, 10)
    step = random.randint(1, 20)
    first_element = random.randint(1, 20)
    progression = generate_progression(step, first_element, lenght)
    index = random.randint(0, lenght)
    correct_value = progression[index]
    missing_number = ".."
    progression[index] = missing_number
    clean_progression = ' '.join(map(str, progression))
    return str(correct_value), clean_progression

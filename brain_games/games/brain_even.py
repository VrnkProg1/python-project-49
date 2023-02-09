from random import randint


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    
def even():
    number = randint(1, 100)
    question = 'Question:'
    if number % 2 == 0:
        correct = True
    elif number % 2 != 0:
        correct = False
    return correct, question, number
    

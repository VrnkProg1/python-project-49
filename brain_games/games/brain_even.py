from random import randint


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    
def even():
    number = randint(1, 100)
    if number % 2 == 0:
        return True
    elif number % 2 != 0:
        return False
    

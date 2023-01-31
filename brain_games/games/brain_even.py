from random import randint

def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def even():
    a = randint(1, 100)
    if a % 2 == 0:
        val = 'yes'
    elif a % 2 != 0:
        val = 'no'
    print('Question:', a)
    return val
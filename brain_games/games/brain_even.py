

def even():
    from random import randint

    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        a = randint(1, 100)
        if a % 2 == 0:
            val = 'yes'
        elif a % 2 != 0:
            val = 'no'
        print('Question: ', a)
        return val

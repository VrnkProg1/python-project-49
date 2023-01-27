def brain_even():
    from random import randint

    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        a = randint(1, 100)
        if a % 2 == 0:
            value = 'yes'
        elif a % 2 != 0:
            value = 'no'
        print('Question: ', a)

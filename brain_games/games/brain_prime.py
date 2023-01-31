import random

def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

def prime():
    k = random.randint(2, 100)
    for i in range(2, int(k/2)+1):
        if (k % i) == 0:
            val = 'no'
            break
        else:
            val = 'yes'
    print('Question:', k)
    return val


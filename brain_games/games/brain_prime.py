import random


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def check():
    number = random.randint(2, 100)
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            print('Question:', number)
            correct = False
            return correct
        else:
            print('Question:', number)
            correct = True
            return correct
    
    
def prime():
    check()
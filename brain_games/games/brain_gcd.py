from random import randint
    

def gcd():
    print('Find the greatest common divisor of given numbers.')
    a = randint(1, 1000)
    b = randint(1, 1000)
    print('Question:', a, b)
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    val = a + b
    return val
    val = string(val)
    
#!/usr/bin/env python3

import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    print('What is the result of the expression?')

    count += 1
    while count < 3:1
        list = ['+', '-', '*']
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        operator = random.choise(list)
        value = value1, operator, value2
        print('Question: ', value)
        answer = prompt.string('Your answer: ')
        if answer == value:
            print('Correct!')
        else:
            print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{value}'")
            print("Let's try again, " + name + '!')
            break
        count += 1
        if count == 3:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()


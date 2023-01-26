#!/usr/bin/env python3

import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    print('What is the result of the expression?')

    count = 0
    while count < 3:
        list = ['+', '-', '*']
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        operator = random.sample(list, 1)
        if operator == ['+']:
            value = value1 + value2
            question1 = f'{value1} {"+"} {value2}'
        elif operator == ['-']:
            value = value1 - value2
            question1 = f'{value1} {"-"} {value2}'
        else:
            value = value1 * value2
            question1 = f'{value1} {"*"} {value2}'
        print('Question: ', question1)
        answer = prompt.string('Your answer: ')
        if int(answer) == value:
            print('Correct!')
        elif int(answer) != value:
            print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{value}'")
            print("Let's try again, " + name + '!')
            break
        count += 1
        if count == 3:
            print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()


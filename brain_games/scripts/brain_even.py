#!/usr/bin/env python3

import prompt
from random import randint


def main():
  print('Welcome to the Brain Games!')
  name = prompt.string('May I have your name? ')
  print('Hello, ', name + '!')
  print('Answer "yes" if the number is even, otherwise answer "no".')

  count = 0
  while count != 3 or answer == value:
      a = randint(1, 100)
      if a % 10 == 0:
          value = 'yes'
      else:
          value = 'no'
      print('Question: ', a)
      answer = prompt.string('Your answer: ')
      if answer == value:
          print('Correct!')
      else:
          print(answer, 'is wrong answer ;(. Correct answer was' + value)
          print("Let's try again, " + name)
      count += 1
   if count == 3: 
       print('Congratulations, ' + name)


if __name__.py == '__main__.py':
    main()

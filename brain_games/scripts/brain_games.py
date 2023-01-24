#!/usr/bin/env python3

import prompt

def main():
    print('Welcome to the Brain Games')
    print('May I have your name? ', end='')
    name = input()
    name = prompt.string('May I have your name?')
    print('Hello,', name, '!')


if __name__ == '__main__':
    main()

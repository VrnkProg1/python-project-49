import prompt

def welcome_user(game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    count = 0
    while count < 3:
        value = game()
        answer = prompt.string('Your answer: ')
        if answer == str(value):
            print('Correct!')
            count += 1
        elif answer != value:
            print(f"'{answer}'", 'is wrong answer ;(. Correct answer was ', f"'{value}'")
            print("Let's try again, " + name + '!')
            break
        if count == 3:
            print('Congratulations, ' + name + '!')

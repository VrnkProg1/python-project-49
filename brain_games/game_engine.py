import prompt


def welcome_user(rulsearg, game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name?')
    print('Hello,', name + '!')
    count = 0
    rulsearg()
    while count < 3:
        value = game()
        answer = prompt.string('Your answer: ')
        wrong = 'is wrong answer ;(. Correct answer was'
        if answer == str(value):
            print('Correct!')
            count += 1
        elif answer != value:
            print(f"'{answer}' {wrong} '{value}'")
            print("Let's try again, " + name + '!')
            break
        if count == 3:
            print('Congratulations, ' + name + '!')

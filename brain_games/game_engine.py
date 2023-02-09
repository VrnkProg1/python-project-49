import prompt


def welcome_user(rulesarg, game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    count = 0
    rulesarg()
    while count < 3:
        value = game()
        print(game())
        if value == False:
            expected_answer = 'no'
        elif value == True:
            expected_answer = 'yes'
        answer = prompt.string('Your answer: ')
        if (value == True and answer == 'yes') or (value == False and answer == 'no'):
            print('Correct!')
            count += 1
        elif (value == False and answer == 'yes') or (value == True and answer == 'no'):
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{expected_answer}'")
            print("Let's try again, " + name + '!')
            break
        if count == 3:
            print('Congratulations, ' + name + '!')

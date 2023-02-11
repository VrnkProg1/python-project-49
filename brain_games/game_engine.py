import prompt


def welcome_user(rulesarg, game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    rulesarg()
    while count < 3:
        correct, question, expression = game()
        print(question, expression)
        if correct == 'True':
            expected_answer = 'yes'
        elif correct == 'False':
            expected_answer = 'no'
        if correct == int():
            expected_answer = correct
        answer = prompt.string('Your answer: ')
        if (correct == 'True' and answer == 'yes') or (correct == 'False' and answer == 'no'):
            print('Correct!')
            count += 1
        elif (correct == 'False' and answer == 'yes') or (correct == 'True' and answer == 'no'):
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{expected_answer}'")
            print("Let's try again, " + name + '!')
            break
        if correct == int() and correct == answer:
            print('Correct!')
            count += 1
        elif correct == int() and correct != answer:
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{expected_answer}'")
            print("Let's try again, " + name + '!')
            break
        if count == 3:
            print('Congratulations, ' + name + '!')

import prompt


def hull_of_game(rulesarg, game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    rules = rulesarg()
    print(rules)
    count = 0
    while count < 3:
        correct, question, expression = game()
        print(question, expression)
        answer = prompt.string('Your answer: ')
        if correct == answer:
            print('Correct!')
            count += 1
        elif correct != answer:
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{correct}'")
            print("Let's try again, " + name + '!')
            return
    print('Congratulations, ' + name + '!')

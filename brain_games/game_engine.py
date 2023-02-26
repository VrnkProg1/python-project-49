import prompt


def get_the_game_and_launch(module):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    rules = module.RULES_OF_THE_GAME()
    print(rules)
    count = 0
    while count < 3:
        correct_answer, expression = module.logic_of_the_game()
        print('Question:', expression)
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            count += 1
        elif correct_answer != answer:
            wrong = 'is wrong answer ;(. Correct answer was'
            print(f"'{answer}' {wrong} '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + name + '!')

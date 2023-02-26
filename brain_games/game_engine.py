import prompt


def launch_game(game_module):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.RULES_OF_GAME)
    count = 0
    while count < 3:
        correct_answer, question = game_module.generate_question_and_answer()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
